import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import sys

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set up API token from environment variable
AIPROXY_TOKEN = os.getenv('AIPROXY_TOKEN')
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN is not set in the environment.")
    sys.exit(1)

# API endpoint and headers
url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AIPROXY_TOKEN}"
}

def read_csv_with_fallback(file_path):
    """
    Attempt to read a CSV file with multiple encodings.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded dataset as a pandas DataFrame.
    """
    encodings = ['utf-8', 'ISO-8859-1', 'latin1', 'utf-16']
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except UnicodeDecodeError:
            pass
    sys.exit(1)

def summarize_data(df):
    """
    Generate a comprehensive summary of the DataFrame.

    Args:
        df (DataFrame): Input pandas DataFrame.

    Returns:
        dict: Summary statistics, missing data, and column-level details.
    """
    summary = {}

    # Basic information
    summary['shape'] = {'rows': df.shape[0], 'columns': df.shape[1]}

    # Column details
    summary['columns'] = {
        column: {
            'data_type': str(df[column].dtype),
            'unique_values': df[column].nunique(),
            'example_values': df[column].dropna().unique()[:5].tolist(),
            'missing_values': df[column].isnull().sum(),
            'missing_percentage': (df[column].isnull().sum() / len(df) * 100)
        }
        for column in df.columns
    }

    # Summary statistics for numerical columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    if not numeric_columns.empty:
        summary['numeric'] = {
            'statistics': df[numeric_columns].describe().to_dict(),
            'correlations': df[numeric_columns].corr().to_dict()
        }

    # Summary statistics for categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    if not categorical_columns.empty:
        summary['categorical'] = {
            'top_values': {
                col: {
                    'most_common_values': df[col].value_counts().head(5).to_dict()
                }
                for col in categorical_columns
            }
        }

    # Missing value overview
    summary['missing_data'] = {
        'total_missing_values': df.isnull().sum().sum(),
        'missing_by_column': df.isnull().sum().to_dict(),
        'columns_with_missing_values': df.columns[df.isnull().any()].tolist()
    }

    # Example rows
    summary['example_rows'] = df.head(3).to_dict(orient='records')

    return summary

def visualize_data(df, output_folder):
    """
    Generate relevant visualizations for meaningful data and save as PNG files.

    Args:
        df (DataFrame): Input pandas DataFrame.
        output_folder (str): Folder to save the visualizations.
    """
    os.makedirs(output_folder, exist_ok=True)

    visualizations = []

    # Replace spaces with underscores in column names
    df.columns = [col.replace(" ", "_") for col in df.columns]

    # Evaluate numerical columns for relevance
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        if df[col].nunique() > 10:  # Ensure dispersion
            std_dev = df[col].std()
            if std_dev > 0.1 * df[col].mean():  # Skip columns with low variance
                visualizations.append(("numeric", col))

    # Evaluate categorical columns for relevance
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_columns:
        if 1 < df[col].nunique() <= 20:  # Avoid constant or high cardinality data
            visualizations.append(("categorical", col))

    # Select top 5 visualizations based on relevance
    selected_visualizations = visualizations[:5]

    # Create the selected visualizations
    for v_type, col in selected_visualizations:
        if v_type == "numeric":
            plt.figure()
            df[col].dropna().hist(bins=30, edgecolor='black', color='skyblue')
            plt.axvline(df[col].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
            plt.axvline(df[col].median(), color='green', linestyle='dashed', linewidth=1, label='Median')
            plt.title(f"Histogram of {col}")
            plt.xlabel(f"{col} (Values)")
            plt.ylabel("Frequency")
            plt.legend()
            plt.savefig(f"{output_folder}/{col}_histogram.png")
            plt.close()

            plt.figure()
            df.boxplot(column=col, vert=True)
            plt.title(f"Boxplot of {col}")
            plt.xlabel(f"{col} (Values)")
            plt.savefig(f"{output_folder}/{col}_boxplot.png")
            plt.close()

        elif v_type == "categorical":
            plt.figure()
            df[col].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
            plt.title(f"Bar Chart of {col}")
            plt.xlabel(f"{col} (Categories)")
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f"{output_folder}/{col}_barchart.png")
            plt.close()

    print(f"Up to 5 relevant visualizations saved in folder: {output_folder}")
    print("Creating README.md file")

def prompt_llm(summary):
    """
    Send a tailored prompt to the LLM with dataset summary only.

    Args:
        summary (dict): Dataset summary.

    Returns:
        str: Response from the LLM.
    """
    numerical_columns = list(summary['numeric']['statistics'].keys()) if 'numeric' in summary else []
    categorical_columns = list(summary['categorical']['top_values'].keys()) if 'categorical' in summary else []
    missing_columns = summary['missing_data'].get('columns_with_missing_values', [])

    # Build a custom prompt based on the dataset summary
    prompt = (
        "I am analyzing a dataset, and here is its summary:\n\n"
        f"### Dataset Shape:\nRows: {summary['shape']['rows']}, Columns: {summary['shape']['columns']}\n\n"
        f"### Column Details:\n"
    )

    if numerical_columns:
        prompt += "#### Numerical Columns:\n"
        for col in numerical_columns:
            stats = summary['numeric']['statistics'][col]
            prompt += (f"- {col}: Mean = {stats['mean']:.2f}, Min = {stats['min']:.2f}, "
                       f"Max = {stats['max']:.2f}, Std Dev = {stats['std']:.2f}\n")
        prompt += "\n"

    if categorical_columns:
        prompt += "#### Categorical Columns:\n"
        for col in categorical_columns:
            top_values = summary['categorical']['top_values'][col]['most_common_values']
            top_values_str = ', '.join([f"{k} ({v})" for k, v in top_values.items()])
            prompt += f"- {col}: Top values: {top_values_str}\n"
        prompt += "\n"

    if missing_columns:
        prompt += f"### Columns with Missing Data ({len(missing_columns)}):\n- {', '.join(missing_columns)}\n\n"

    prompt += (
        "### Questions for Analysis:\n"
        "1. What key patterns or trends do you observe in the data?\n"
        "2. Are there specific correlations or insights based on the numerical and categorical columns?\n"
        "3. How should I address missing values or potential outliers?\n"
        "4. What additional analyses can I perform to uncover further insights from this dataset?\n"
        "5. Suggest actionable steps or improvements based on the data structure and features.\n\n"
    )

    # Final payload
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [])[0].get("message", {}).get("content", "No response.")
    except Exception as e:
        print(f"Error communicating with LLM: {e}")
        return None

def save_to_readme(output_folder, llm_response):
    """
    Save the LLM response and generated visualizations to a README.md file.

    Args:
        output_folder (str): Folder to save the README.md file.
        llm_response (str): Response from the LLM.
    """
    readme_content = f"""# Dataset Analysis Report

{llm_response}

## Visualizations
"""
    
    image_files = [file for file in os.listdir(output_folder) if file.endswith(".png")]
    for image in image_files:
        readme_content += f"![{image}]({image})\n\n"

    readme_path = os.path.join(output_folder, "README.md")
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content)

    print(f"README.md created at {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: The dataset file '{file_path}' does not exist.")
        sys.exit(1)

    try:
        df = read_csv_with_fallback(file_path)
        summary = summarize_data(df)

        output_folder = os.path.splitext(file_path)[0]
        visualize_data(df, output_folder)

        response = prompt_llm(summary)

        save_to_readme(output_folder, response)

    except Exception as e:
        print(f"An error occurred: {e}")