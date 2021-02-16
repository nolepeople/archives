import pandas as pd

csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")

print(csv_data['Age'].iloc[1])
print ("\n\n")
print(csv_data.head())
