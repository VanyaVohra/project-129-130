import csv
import pandas as pd

df = pd.read_csv("merged.csv")
print(df.shape)

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Luminosity"]
print(df.shape)
print(list(df))
