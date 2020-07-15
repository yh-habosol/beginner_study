import pandas as pd

df = pd.read_csv("./auto-mpg.csv", header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head())
print("\n")
print(df.tail())


print(df.shape, "\n")

print(df.info(), "\n")

print(df.dtypes, "\n")

print(df.describe(), "\n")

print(df.describe(include="all"), "\n")

print(df.count(), "\n")

print(df["origin"].value_counts())