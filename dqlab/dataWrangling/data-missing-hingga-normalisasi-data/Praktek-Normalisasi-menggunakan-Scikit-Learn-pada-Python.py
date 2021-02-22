"""
Scikit Learn merupakan library pada python yang digunakan untuk machine learning 
dan data science. Salah satu library yang selalu menjadi favorit dan komunitasnya 
sangat kuat. Scikit-learn sendiri tidak hanya untuk analytics saja, namun juga 
untuk pre-processing, feature selection, dan proses analysis lainnya. Melanjutkan 
dari sesi normalisasi data, mari kita praktekan kode di bawah ini :
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing

csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")
array = csv_data.values

#X merupakan matriks yang berisi fitur dataset yang akan digunakan dalam machine learning, baik untuk regresi, klasifikasi, pengklusteran, atau normalisasi
#Pada kasus kita, X berisi fitur-fitur yang digunakan untuk dinormalisasi dengan teknik min-max scaler
#Ketik lanjutan dari kode di atas:

X = array[:,2:5] #memisahkan fitur dari dataset. 
Y = array[:,0:1]  #memisahkan class dari dataset

dataset=pd.DataFrame({'Customer ID':array[:,0],'Gender':array[:,1],'Age':array[:,2],'Income':array[:,3],'Spending Score':array[:,4]})
print("dataset sebelum dinormalisasi :")
print(dataset.head(10))

min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1)) #inisialisasi normalisasi MinMax
data = min_max_scaler.fit_transform(X) #transformasi MinMax untuk fitur
dataset = pd.DataFrame({'Age':data[:,0],'Income':data[:,1],'Spending Score':data[:,2],'Customer ID':array[:,0],'Gender':array[:,1]})

print("dataset setelah dinormalisasi :")
print(dataset.head(10))

"""
Hasil pada panel console akan keluar seperti berikut :

dataset sebelum dinormalisasi :
  Age Customer ID  Gender Income Spending Score
0  19           1    Male     15             39
1  21           2    Male     15             81
2  20           3  Female     16              6
3  23           4  Female     16             77
4  31           5  Female     17             40
5  22           6  Female     17             76
6  35           7  Female     18              6
7  23           8  Female     18             94
8  64           9    Male     19              3
9  30          10  Female     19             72
dataset setelah dinormalisasi :
        Age Customer ID  Gender    Income  Spending Score
0  0.019231           1    Male  0.000000        0.387755
1  0.057692           2    Male  0.000000        0.816327
2  0.038462           3  Female  0.008197        0.051020
3  0.096154           4  Female  0.008197        0.775510
4  0.250000           5  Female  0.016393        0.397959
5  0.076923           6  Female  0.016393        0.765306
6  0.326923           7  Female  0.024590        0.051020
7  0.096154           8  Female  0.024590        0.948980
8  0.884615           9    Male  0.032787        0.020408
9  0.230769          10  Female  0.032787        0.724490
"""
