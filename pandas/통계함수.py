import pandas as pd

df = pd.read_csv("./auto-mpg.csv", header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']


print(df.mean(), "\n")

print(df["mpg"].mean(), "\n")

print(df[["mpg", "weight"]].mean(), "\n")


print(df.median(), "\n")

print(df["mpg"].median(), "\n")


print(df.max(), "\n")

print(df["mpg"].max(), "\n")


print(df.min(), "\n")

print(df["mpg"].min(), "\n")


print(df.std(), "\n")

print(df["mpg"].std(), "\n")


print(df.corr(), "\n")

print(df[["mpg", "weight"]].corr(), "\n")
