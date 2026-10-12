import pandas as pd

data = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")
print(data.head())
data.info()
print(data.describe())
numeric = data.select_dtypes(include="number")
print(numeric.mean())
print(numeric.median())
print(numeric.mode().iloc[0])
print(numeric.std())
print(numeric.corr())
