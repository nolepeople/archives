import pandas as pd

csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")
print("Menampilkan data ke 5 sampai kurang dari 10 :")
print(csv_data['Age'].iloc[5:10])



csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")
print("Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris:")
print(csv_data.iloc[5:10])
