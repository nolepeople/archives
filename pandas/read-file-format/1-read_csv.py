# umum nya nilai dalam format csv dipisahkan oleh koma
# sehingga fungsi seperator read_csv() adalah koma
# Jika nilai tidak terpisah oleh koma maka harus ditambahkan parameter separator
# kita gunakan titik koma ; untuk seperator nya
# contoh file dataset/dataku.csv

import pandas as pd

print ("\n[*] pemisahan titik koma untuk fieldnya\n")
data = pd.read_csv("dataset/dataku.csv",sep=";")
print (data)

print ("\n[*] output tanpa seperator\n")
data = pd.read_csv("dataset/dataku.csv")
print (data)

print ("\n[*] mengubah baris pertama tidak menjadi header\n")
data = pd.read_csv("dataset/dataku.csv",header=None,sep=";")
print (data)

print ("\n[*] mengubah header name dengan names \n")
data = pd.read_csv("dataset/dataku.csv",sep=";",names=["name","address"])
print (data)
