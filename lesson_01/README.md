
# Lesson 1: Python and Pandas fundamentals

## [Problem 4](problem_04.ipynb): PARLA

### Problem
- The goal was to analyze the average time between a user's visit to the website and the corresponding purchase:
    - A visit is considered related to a purchase if it occurred no earlier than two hours before the purchase.
    - I.e. for each purchase I needed to calculate the time between the purchase and the earliest website visit by the same user within the two hours prior to the purchase.
    - Then, compute the average of these time intervals.

### Action
- I loaded web-logs data and sales data from CSV files.
- I filtered and ordered the data.
- I merged, filtered and transformed the datasets into a single dataset.
- I calculated average interval by grouping and aggregating the dataset.

### Result
- I successfully calculated the average interval between login and sale.

### Learning
- I revised relevant python and pandas functions.
- I revised working with datetime and time deltas in Pandas.
- I revised joining and aligning of dataframes.

### Application
- I can apply relevant Python and Pandas functions in similar data-analysis scenarios.



## [Problem 7](problem_07.ipynb): PARLA

### Problem
- Write a function that filters dataframe, using provided parameters

### Action
- I implemented the function, using relevant Python and Pandas functionality

### Result
- The function was successfully implemented and passed all tests

### Learning
- I revised relevant Python and Pandas functionality

### Application
- I can apply the relevant Python and Pandas functionality for data-related problems



## [Problem 8](problem_08.ipynb): PARLA

### Problem
- Write a function that computes server response times within a given date range
- Write a function that calculates total user revenue during a specified period for users who visited the website during the specified period
- Write a function that calculates total revenue per user for a specified period, and only for users who visited the website at any time before 'end_date'

### Action
- I implemented these functions, using relevant Python and Pandas functionality

### Result
- All functions successfully passed all tests

### Learning
- I revised relevant Python and Pandas functionality

### Application
- I can apply the relevant Python and Pandas functionality for data-related problems
