# Selain melakukan akses data melalui kolom, dengan menggunakan pandas juga bisa melakukan akses dengan menggunakan baris. Berbeda dengan akses melalui kolom, fungsi untuk menampilkan data dari suatu baris adalah fungsi .iloc[i] dimana [i] menunjukan urutan baris yang akan ditampilkan yang dimana indexnya diawali dari 0. Coba ketikan code di bawah ini untuk mempermudah :

import pandas as pd
csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")
print (csv_data.iloc[5])
