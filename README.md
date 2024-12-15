# Dataset Analysis

## Summary

### Shape of the Dataset
(10000, 23)

### Column Information
{
    "book_id": "int64",
    "goodreads_book_id": "int64",
    "best_book_id": "int64",
    "work_id": "int64",
    "books_count": "int64",
    "isbn": "object",
    "isbn13": "float64",
    "authors": "object",
    "original_publication_year": "float64",
    "original_title": "object",
    "title": "object",
    "language_code": "object",
    "average_rating": "float64",
    "ratings_count": "int64",
    "work_ratings_count": "int64",
    "work_text_reviews_count": "int64",
    "ratings_1": "int64",
    "ratings_2": "int64",
    "ratings_3": "int64",
    "ratings_4": "int64",
    "ratings_5": "int64",
    "image_url": "object",
    "small_image_url": "object"
}

### Missing Values
{
    "book_id": 0,
    "goodreads_book_id": 0,
    "best_book_id": 0,
    "work_id": 0,
    "books_count": 0,
    "isbn": 700,
    "isbn13": 585,
    "authors": 0,
    "original_publication_year": 21,
    "original_title": 585,
    "title": 0,
    "language_code": 1084,
    "average_rating": 0,
    "ratings_count": 0,
    "work_ratings_count": 0,
    "work_text_reviews_count": 0,
    "ratings_1": 0,
    "ratings_2": 0,
    "ratings_3": 0,
    "ratings_4": 0,
    "ratings_5": 0,
    "image_url": 0,
    "small_image_url": 0
}

### Summary Statistics

{
    "book_id": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 5000.5,
        "std": 2886.8956799071675,
        "min": 1.0,
        "25%": 2500.75,
        "50%": 5000.5,
        "75%": 7500.25,
        "max": 10000.0
    },
    "goodreads_book_id": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 5264696.5132,
        "std": 7575461.863589611,
        "min": 1.0,
        "25%": 46275.75,
        "50%": 394965.5,
        "75%": 9382225.25,
        "max": 33288638.0
    },
    "best_book_id": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 5471213.5801,
        "std": 7827329.890719961,
        "min": 1.0,
        "25%": 47911.75,
        "50%": 425123.5,
        "75%": 9636112.5,
        "max": 35534230.0
    },
    "work_id": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 8646183.4246,
        "std": 11751060.824080039,
        "min": 87.0,
        "25%": 1008841.0,
        "50%": 2719524.5,
        "75%": 14517748.25,
        "max": 56399597.0
    },
    "books_count": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 75.7127,
        "std": 170.47072765025834,
        "min": 1.0,
        "25%": 23.0,
        "50%": 40.0,
        "75%": 67.0,
        "max": 3455.0
    },
    "isbn": {
        "count": 9300,
        "unique": 9300,
        "top": "375700455",
        "freq": 1,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    },
    "isbn13": {
        "count": 9415.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 9755044298883.463,
        "std": 442861920665.57336,
        "min": 195170342.0,
        "25%": 9780316192995.0,
        "50%": 9780451528640.0,
        "75%": 9780830777175.0,
        "max": 9790007672390.0
    },
    "authors": {
        "count": 10000,
        "unique": 4664,
        "top": "Stephen King",
        "freq": 60,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    },
    "original_publication_year": {
        "count": 9979.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 1981.987674115643,
        "std": 152.57666516754668,
        "min": -1750.0,
        "25%": 1990.0,
        "50%": 2004.0,
        "75%": 2011.0,
        "max": 2017.0
    },
    "original_title": {
        "count": 9415,
        "unique": 9274,
        "top": " ",
        "freq": 5,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    },
    "title": {
        "count": 10000,
        "unique": 9964,
        "top": "Selected Poems",
        "freq": 4,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    },
    "language_code": {
        "count": 8916,
        "unique": 25,
        "top": "eng",
        "freq": 6341,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    },
    "average_rating": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 4.002191000000001,
        "std": 0.25442748053872905,
        "min": 2.47,
        "25%": 3.85,
        "50%": 4.02,
        "75%": 4.18,
        "max": 4.82
    },
    "ratings_count": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 54001.2351,
        "std": 157369.95643554674,
        "min": 2716.0,
        "25%": 13568.75,
        "50%": 21155.5,
        "75%": 41053.5,
        "max": 4780653.0
    },
    "work_ratings_count": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 59687.3216,
        "std": 167803.7852374182,
        "min": 5510.0,
        "25%": 15438.75,
        "50%": 23832.5,
        "75%": 45915.0,
        "max": 4942365.0
    },
    "work_text_reviews_count": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 2919.9553,
        "std": 6124.378131569911,
        "min": 3.0,
        "25%": 694.0,
        "50%": 1402.0,
        "75%": 2744.25,
        "max": 155254.0
    },
    "ratings_1": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 1345.0406,
        "std": 6635.626262783459,
        "min": 11.0,
        "25%": 196.0,
        "50%": 391.0,
        "75%": 885.0,
        "max": 456191.0
    },
    "ratings_2": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 3110.885,
        "std": 9717.123578396993,
        "min": 30.0,
        "25%": 656.0,
        "50%": 1163.0,
        "75%": 2353.25,
        "max": 436802.0
    },
    "ratings_3": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 11475.8938,
        "std": 28546.449183182456,
        "min": 323.0,
        "25%": 3112.0,
        "50%": 4894.0,
        "75%": 9287.0,
        "max": 793319.0
    },
    "ratings_4": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 19965.6966,
        "std": 51447.35838380058,
        "min": 750.0,
        "25%": 5405.75,
        "50%": 8269.5,
        "75%": 16023.5,
        "max": 1481305.0
    },
    "ratings_5": {
        "count": 10000.0,
        "unique": NaN,
        "top": NaN,
        "freq": NaN,
        "mean": 23789.8056,
        "std": 79768.88561077163,
        "min": 754.0,
        "25%": 5334.0,
        "50%": 8836.0,
        "75%": 17304.5,
        "max": 3011543.0
    },
    "image_url": {
        "count": 10000,
        "unique": 6669,
        "top": "https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png",
        "freq": 3332,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    },
    "small_image_url": {
        "count": 10000,
        "unique": 6669,
        "top": "https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png",
        "freq": 3332,
        "mean": NaN,
        "std": NaN,
        "min": NaN,
        "25%": NaN,
        "50%": NaN,
        "75%": NaN,
        "max": NaN
    }
}

### Example Rows

[
    {
        "book_id": 1,
        "goodreads_book_id": 2767052,
        "best_book_id": 2767052,
        "work_id": 2792775,
        "books_count": 272,
        "isbn": "439023483",
        "isbn13": 9780439023480.0,
        "authors": "Suzanne Collins",
        "original_publication_year": 2008.0,
        "original_title": "The Hunger Games",
        "title": "The Hunger Games (The Hunger Games, #1)",
        "language_code": "eng",
        "average_rating": 4.34,
        "ratings_count": 4780653,
        "work_ratings_count": 4942365,
        "work_text_reviews_count": 155254,
        "ratings_1": 66715,
        "ratings_2": 127936,
        "ratings_3": 560092,
        "ratings_4": 1481305,
        "ratings_5": 2706317,
        "image_url": "https://images.gr-assets.com/books/1447303603m/2767052.jpg",
        "small_image_url": "https://images.gr-assets.com/books/1447303603s/2767052.jpg"
    },
    {
        "book_id": 2,
        "goodreads_book_id": 3,
        "best_book_id": 3,
        "work_id": 4640799,
        "books_count": 491,
        "isbn": "439554934",
        "isbn13": 9780439554930.0,
        "authors": "J.K. Rowling, Mary GrandPr\u00e9",
        "original_publication_year": 1997.0,
        "original_title": "Harry Potter and the Philosopher's Stone",
        "title": "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)",
        "language_code": "eng",
        "average_rating": 4.44,
        "ratings_count": 4602479,
        "work_ratings_count": 4800065,
        "work_text_reviews_count": 75867,
        "ratings_1": 75504,
        "ratings_2": 101676,
        "ratings_3": 455024,
        "ratings_4": 1156318,
        "ratings_5": 3011543,
        "image_url": "https://images.gr-assets.com/books/1474154022m/3.jpg",
        "small_image_url": "https://images.gr-assets.com/books/1474154022s/3.jpg"
    },
    {
        "book_id": 3,
        "goodreads_book_id": 41865,
        "best_book_id": 41865,
        "work_id": 3212258,
        "books_count": 226,
        "isbn": "316015849",
        "isbn13": 9780316015840.0,
        "authors": "Stephenie Meyer",
        "original_publication_year": 2005.0,
        "original_title": "Twilight",
        "title": "Twilight (Twilight, #1)",
        "language_code": "en-US",
        "average_rating": 3.57,
        "ratings_count": 3866839,
        "work_ratings_count": 3916824,
        "work_text_reviews_count": 95009,
        "ratings_1": 456191,
        "ratings_2": 436802,
        "ratings_3": 793319,
        "ratings_4": 875073,
        "ratings_5": 1355439,
        "image_url": "https://images.gr-assets.com/books/1361039443m/41865.jpg",
        "small_image_url": "https://images.gr-assets.com/books/1361039443s/41865.jpg"
    }
]

## LLM Suggestions

Given the structure of your dataset and the information provided, there are several types of analyses you can perform. Here are some suggestions across various analytical dimensions:

### Descriptive Analysis

1. **Missing Values Handling**:
   - Investigate the columns with missing values (e.g., `isbn`, `isbn13`, `original_publication_year`, `original_title`, `language_code`). Decide whether to fill these values, ignore the rows, or drop the columns based on their significance in your analysis.

2. **Distribution of Ratings**:
   - Visualize the distribution of `average_rating` using histograms or box plots.
   - Analyze the distribution of `ratings_count` to identify popular books versus niche books.

3. **Popularity Metrics**:
   - Calculate the number of reviews and average ratings for books to see which titles are the most popular.
   - Identify the most frequently rated books (`ratings_count`) and the books with the highest average ratings.

### Inferential Analysis

4. **Correlation Analysis**:
   - Investigate correlations between numerical variables like `average_rating`, `ratings_count`, and different star ratings (e.g., `ratings_1`, `ratings_2`, etc.).
   - Use a heatmap to visualize these correlations and identify variables that are strongly correlated.

5. **Group Analysis**:
   - Group the data by `authors` or `original_publication_year` and analyze average ratings and rating counts to see trends over time or by popular authors.
   - Assess how the publication year affects the average rating or number of ratings.

### Textual Analysis

6. **Natural Language Processing (NLP)**:
   - Perform textual analysis on the `title` and `original_title` columns to identify trends in naming conventions, such as the presence of series names or genre indications.
   - Analyze the diversity of authors to see how many unique authors are contributing to book ratings, and categorizing them by behaviors like average ratings.

### Comparative Analysis

7. **Language Analysis**:
   - Compare the average ratings across different `language_code` groups to explore how language may influence book ratings.
   - Examine which languages have the most books published and how those books tend to be rated.

8. **Category-based Analysis (if applicable)**:
   - If you have access to genre or category information (not shown in your current dataset), analyze which genres have higher average ratings or greater counts.

### Predictive Analysis

9. **Predictive Modeling**:
   - Build a predictive model to forecast future ratings based on historical data using regression analysis. Input features could include `books_count`, `original_publication_year`, and others.
   - If you have sufficient historical data, train models to predict ratings or reviews for upcoming books based on existing characteristics.

### Visualization

10. **Visualizations**:
    - Create visualizations for the findings, such as:
      - Bar charts showing the top-rated books.
      - Line plots showing trends in ratings per year.
      - Word clouds from titles and authors to visualize popular terms.

### Conclusion and Insights

11. **Summarize Findings**:
    - Conclude your analysis with actionable insights. For example, if certain authors consistently produce high-rated titles, this could inform marketing or acquisition strategies.

By covering a range of analyses from descriptive to predictive, you can gain a comprehensive understanding of the dataset and derive meaningful insights related to books and their ratings.

## Visualizations

![average_rating_boxplot.png](./visualizations/average_rating_boxplot.png)

![average_rating_histogram.png](./visualizations/average_rating_histogram.png)

![best_book_id_boxplot.png](./visualizations/best_book_id_boxplot.png)

![best_book_id_histogram.png](./visualizations/best_book_id_histogram.png)

![books_count_boxplot.png](./visualizations/books_count_boxplot.png)

![books_count_histogram.png](./visualizations/books_count_histogram.png)

![book_id_boxplot.png](./visualizations/book_id_boxplot.png)

![book_id_histogram.png](./visualizations/book_id_histogram.png)

![correlation_matrix.png](./visualizations/correlation_matrix.png)

![goodreads_book_id_boxplot.png](./visualizations/goodreads_book_id_boxplot.png)

![goodreads_book_id_histogram.png](./visualizations/goodreads_book_id_histogram.png)

![isbn13_boxplot.png](./visualizations/isbn13_boxplot.png)

![isbn13_histogram.png](./visualizations/isbn13_histogram.png)

![original_publication_year_boxplot.png](./visualizations/original_publication_year_boxplot.png)

![original_publication_year_histogram.png](./visualizations/original_publication_year_histogram.png)

![ratings_1_boxplot.png](./visualizations/ratings_1_boxplot.png)

![ratings_1_histogram.png](./visualizations/ratings_1_histogram.png)

![ratings_2_boxplot.png](./visualizations/ratings_2_boxplot.png)

![ratings_2_histogram.png](./visualizations/ratings_2_histogram.png)

![ratings_3_boxplot.png](./visualizations/ratings_3_boxplot.png)

![ratings_3_histogram.png](./visualizations/ratings_3_histogram.png)

![ratings_4_boxplot.png](./visualizations/ratings_4_boxplot.png)

![ratings_4_histogram.png](./visualizations/ratings_4_histogram.png)

![ratings_5_boxplot.png](./visualizations/ratings_5_boxplot.png)

![ratings_5_histogram.png](./visualizations/ratings_5_histogram.png)

![ratings_count_boxplot.png](./visualizations/ratings_count_boxplot.png)

![ratings_count_histogram.png](./visualizations/ratings_count_histogram.png)

![work_id_boxplot.png](./visualizations/work_id_boxplot.png)

![work_id_histogram.png](./visualizations/work_id_histogram.png)

![work_ratings_count_boxplot.png](./visualizations/work_ratings_count_boxplot.png)

![work_ratings_count_histogram.png](./visualizations/work_ratings_count_histogram.png)

![work_text_reviews_count_boxplot.png](./visualizations/work_text_reviews_count_boxplot.png)

![work_text_reviews_count_histogram.png](./visualizations/work_text_reviews_count_histogram.png)

