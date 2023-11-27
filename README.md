# ML-project-on-Movie-recommendation-system
# Movie Recommendation System

This project involves building a movie recommendation system using collaborative filtering on the MovieLens 100k dataset.

## Overview

This Python script provides functionalities for:

- Loading and exploring MovieLens 100k dataset.
- Analyzing movie ratings and user interactions.
- Building a movie recommendation system based on user ratings and correlations between movies.

## Requirements

- Python 3.x
- Required Libraries: numpy, pandas, matplotlib, seaborn

## Usage

1. **Setup:**

    - Ensure Python 3.x is installed.
    - Install required libraries using pip:
        ```bash
        pip install numpy pandas matplotlib seaborn
        ```

2. **Dataset:**

    - The MovieLens 100k dataset is used (`ml-100k/u.data` and `ml-100k/u.item`).
    - Ensure these files are placed in the correct directory as specified in the code (`movie_data/ml-100k/`).

3. **Running the Code:**

    - Run the Python script in a compatible environment (e.g., Jupyter Notebook, Python IDE).
    - Execute the cells to perform the following tasks:
        - Loading and exploring the dataset.
        - Analyzing movie ratings and interactions.
        - Building the movie recommendation system.
        - Generating movie recommendations based on provided movie names.

## How to Use

1. Execute the code cells in a Python environment or Jupyter Notebook.
2. Functions available:
    - `recommend(movie_name)`: Pass the movie name to get recommendations based on correlations.

Example Usage:
```python
recommend("12 Angry Men (1957)")
