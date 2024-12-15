Autolysis: Automated Dataset Analysis
Project Overview
The Autolysis project automates the process of analyzing, visualizing, and narrating insights from datasets. It leverages Python's data processing and visualization libraries combined with a language model (GPT-4o-Mini) to generate meaningful narratives and actionable insights.

Key Features
Flexible Input: Accepts any valid CSV file as input.
Automated Analysis: Computes summary statistics, detects missing data, and analyzes correlations and patterns.
Data Visualization: Generates up to five visualizations in PNG format to support the analysis.
LLM Integration: Utilizes GPT-4o-Mini to narrate findings and suggest deeper analyses.
Markdown Report: Outputs the analysis and visualizations in a single README.md file for easy review.
Usage Instructions
Requirements
Python 3.8+ installed.
Required Python libraries:
pandas
numpy
matplotlib
requests
dotenv
An AI Proxy Token set in the environment variable AIPROXY_TOKEN.
Setup
Clone this repository:

bash
Copy code
git clone https://github.com/[your-repo]/autolysis.git
cd autolysis
Install the required libraries:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project directory and set your AI Proxy Token:

plaintext
Copy code
AIPROXY_TOKEN=your_token_here
Run the Script
To analyze a dataset, use:

bash
Copy code
uv run autolysis.py <dataset.csv>
For example:

bash
Copy code
uv run autolysis.py goodreads.csv
Outputs
Upon running the script:

A README.md file will be created in a directory named after the input dataset (e.g., goodreads/README.md).
Up to five PNG visualizations will be saved in the same directory.
Project Structure
autolysis.py: The main script for dataset analysis, visualization, and narration.
.env: Contains the AIPROXY_TOKEN (not committed to the repository).
Dataset folders:
goodreads/
happiness/
media/
Each folder contains:

A README.md with the analysis narrative and embedded visualizations.
PNG files of the generated charts.
Features in Detail
Data Analysis
The script performs the following:

Summarizes the shape, columns, and data types.
Identifies missing values and calculates their percentage.
Generates summary statistics for numerical and categorical columns.
Detects correlations between numerical columns.
Data Visualization
Up to five visualizations are generated based on relevance:

Histograms and boxplots for numerical columns.
Bar charts for categorical columns.
LLM Integration
The script utilizes GPT-4o-Mini for:

Interpreting dataset summaries.
Generating a narrative with insights and implications.
Suggesting additional analyses to explore.
Markdown Report
The narrative and visualizations are combined in a single README.md file, providing:

An overview of the dataset.
Analytical insights.
Visualization summaries.
Example Use Cases
Goodreads Dataset:

Discover patterns in book ratings and author dominance.
Analyze trends across publication years.
Happiness Dataset:

Correlate happiness scores with GDP and life expectancy.
Cluster countries based on their scores.
Media Dataset:

Analyze faculty preferences for books, movies, and TV series.
Visualize ratings distribution for different media categories.
Evaluation Criteria
This project is evaluated on:

Functionality: Successful execution for different datasets without errors.
Code Quality: Clean, modular, and efficient code.
Outputs: Well-structured narratives and meaningful visualizations.
Uniqueness: Creativity and diverse analyses for datasets.
Engagement: Insightful, actionable, and visually appealing results.
License
This project is released under the MIT License. Feel free to use, modify, and distribute it.
