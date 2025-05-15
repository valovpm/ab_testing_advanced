
# Lesson 2: Hypothesis testing

## [Problem 2](problem_02.ipynb): PARLA

### Problem
- Write a function that:
    - performs independent t-test using provided control and experimental groups
    - rounds the resulting p-value to the third decimal place
- Analyze the significance of the difference in average revenue per user (ARPU):
    - select the week before the experiment (from 2022-03-16 to 2022-03-23).
    - Use the data from the files 2022-04-01T12_df_sales.csv and experiment_users.csv to solve the task.
    - Perform independent t-test using the previous function.

### Action
- Implemented 'get_ttest_pvalue()' function, using relevant Python, Numpy, and Scipy functionality.
- Analyzed significance of ARPU difference:
    - I loaded, filtered, merged, grouped, aggregated, and sorted original dataframes.
    - I replaced missing values with zeros.
    - Created control and experimental groups, by filtering the merged dataframe.
    - Performed independent t-test using control and experimental groups.

### Result
- Successfully tested 'get_ttest_pvalue()' function.
- Demonstrated that ARPU difference between control and experimental groups is not significant, by calculating a p-value (0.199) that is much larger than the standard significance level (0.05).

### Learning
- I revised relevant Python, Numpy, Pandas, and Scipy functionality.
- I realized that handing of missing data is important (omission of missing values instead of replacing them with zeros changes p-value).
- I learned how to perform independent t-tests.

### Application
- I can apply relevant Python and Pandas functionality for data-related problems.
- I can apply independent t-tests in practice.



## [Problem 3](problem_03.ipynb): PARLA

### Problem
- Estimate the average time between purchases:
    - Take all customers who made 2 or more purchases.
    - Calculate the time between purchases (a customer with N purchases should have N–1 time intervals).
    - Combine the time intervals of all customers and compute the average.
- Use the data from the file '2022-04-01T12_df_sales.csv' to solve the task.
- Provide the average number of days between purchases, rounded to the nearest whole number.

### Action
- I estimated the average time between purchases using relevant Python, and Pandas functionality
- I loaded, filtered, grouped, aggregated, and sorted original dataframe
- I created dataframe, where dates for each user are shifted
- I merged dataframes to calculate time deltas

### Result
- Successfully calculated average time between purchases for active users

### Learning
- I revised relevant Python and Pandas functionality
- I revised working with 'datetime' data type

### Application
- I can apply relevant Python and Pandas functionality for similar data-related problems

