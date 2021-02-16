#Dengan menggunakan fungsi pandas, kita tidak perlu melihat satu persatu baris data untuk mengetahui apakah ada nilai kosong atau NULL/NAN pada suatu dataset. Bayangkan jika kita memilki 1000 baris data. Apakah kita harus melihat semua baris data tersebut? Tentu saja tidak. Maka dari itu di pandas disediakan fungsi untuk mengecek apakah ada data yang kosong. Coba praktikkan kode di bawah ini :
import pandas as pd

#data non-missing value : False
csv_data = pd.read_csv("http://academy.dqlab.id/dataset/shopping_data.csv")
print(csv_data.isnull().values.any())

#data missing value : True
csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data_missingvalue.csv")
print(csv_data.isnull().values.any())

