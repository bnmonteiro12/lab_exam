import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("b5_output1.csv")
df['Average counts'] = df['J'].iloc[4:6, 34:37, 42:44, 56:58].mean()

print (df)