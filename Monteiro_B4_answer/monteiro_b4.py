import pandas as pd

data = pd.read_csv("b4_output1.csv")
g = df['Scientific Name'].unique()
x = data.iloc[:,2]
y = x.drop_duplicates()
y.to_csv('yah.csv')
df['Average counts'] = df['L'].iloc[2:4].mean()

print(df)