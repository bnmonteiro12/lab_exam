import pandas as pd
import numpy as np

df = pd.read_csv("b7_output1.csv")
tdf = df.T

print(tdf.head())
print (df)

df.to_csv("table1.csv",index=False)