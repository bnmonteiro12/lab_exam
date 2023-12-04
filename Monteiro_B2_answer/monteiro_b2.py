import pandas as pd

data = pd.read_csv("b2_output1.csv", index_col="Genus")
rows = data.loc[["St"]]
print(type(rows))
rows
print (df)