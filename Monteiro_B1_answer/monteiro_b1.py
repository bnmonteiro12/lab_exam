import pandas as pd

data = pd.read_csv("b1_output1.csv", index_col="Interval")
rows = data.loc[["30-0"]]
print(type(rows))
rows
print (df)