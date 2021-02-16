# mean = nilai rata2, median = nilai tengah ( a + b ) / c
import pandas as pd

dataCsv = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data_missingvalue.csv")

# nilai rata rata dari mean func
print (dataCsv.mean())
#nilai rata rata dari median func
print (dataCsv.median())


print ("data none yang belum diisi")
print (dataCsv.head())
print ("data yang sudah diisi")
print (dataCsv.head().fillna(dataCsv.mean()))
print (dataCsv.head().fillna(dataCsv.median()))



