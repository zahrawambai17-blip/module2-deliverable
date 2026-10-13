# Obesity Dataset Analysis

This is a Python script that examines a small public data set of eating habits, physical condition, obesity and calculates simple statistics for the numerical features.

# Dataset
File: ObesityDataSet_raw_and_data_sinthetic.csv
Description: The text is approximately 2,111 rows by 17 columns; there are no missing values.
Alberta Health Services (AHS) launched their health system modernization initiative in 2008.In 2008, Alberta Health Services (AHS) began their health system modernization initiative.
Text columns (9): Gender, family_history_with_overweight, FAVC, CAEC, SMOKE, SCC, CALC, MTRANS, NObeyesdad
Note: This dataset has some synthetic (software-generated) rows, and the survey columns have decimal values.

# Requirements
Python 3.8 
pandas library

# How to run
1. Put the CSV file in the same folder as the script.
2. Open a terminal and navigate to the folder using "cd"
3. Run using: "python modul2.py"

# How it works

It uses pd.read_csv() to read the CSV into a DataFrame and the select_dtypes(include="number") to filter out non-numeric columns. Each column has its mean, median, mode calculated using a built-in pandas function, as well as its standard deviation and correlation.

# Result
1. There is a median of 22.8, and a mean of 24.3, which is pulled up by a few old people; for Age.
2. The strongest relationship is between Height and Weight (0.46) which is a moderate positive correlation.
3. The most negative correlation with TUE is with age (-0.30).
4. None of the features show strong correlation (less than 0.5).
