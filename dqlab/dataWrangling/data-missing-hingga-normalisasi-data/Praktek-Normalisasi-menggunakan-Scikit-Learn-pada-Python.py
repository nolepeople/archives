import pandas as pd
import numpy as np
from sklearn import preprocessing


dataCsv =  pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")
arrayMatrix = dataCsv.values

X =  arrayMatrix[:,2:5]
Y = arrayMatrix[:,0:1]






