import pandas as pd

data = pd.read_csv("b3_output1.csv")
g = df['Scientific Name'].unique()
x = data.iloc[:,2]
y = x.drop_duplicates()
y.to_csv('yah.csv')

print(df)