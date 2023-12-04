import pandas as pd
import numpy as np

df = pd.read_csv("b6_output1.csv")
df.insert(0, "HRID")
df["HRID"] = df['Location'].astype(str) +"-"+ df['Site'].astype(str) +"-" + df['Replicate'].astype(str)

print(df)