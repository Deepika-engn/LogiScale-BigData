import pandas as pd

df = pd.read_csv("data/data.csv")

print(df.head())

print("Total Rows:", len(df))

print(df.info())

print(df.describe())