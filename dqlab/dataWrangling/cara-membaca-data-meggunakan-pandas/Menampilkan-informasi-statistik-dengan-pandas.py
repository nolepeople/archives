#Mengetahui informasi statistik pada suatu data sangat penting. Mulai dari distribusi data, nilai max atau min, hingga standar deviasi dari suatu dataset. Jika datanya berjumlah dibawah 10 mungkin masih dikerjakan secara manual. Namun, bayangkan jika datanya sudah mencapai ratusan bahkan ribuan. Tidak mungkin pastinya untuk dilakukan secara manual. Maka dari itu pentingnya fungsi describe() pada pandas. Fungsi describe() ini memungkinkan untuk mengetahui informasi statistik dari suatu dataset secara cepat. Coba untuk ketikkan kode di bawah ini :

import pandas as pd

file = "https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv"

csv_data = pd.read_csv(file)
print (csv_data.describe(include="all"))
#kecualikan nilai string untuk filtering NaN / non-numerical
print (csv_data.describe(exclude="O"))

