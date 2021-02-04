import pandas as pd


dataset = pd.read_csv("dataset/anime.csv")

print ("[*] kolum nya ada 7 value termasuk class",end="\n")
print (dataset.columns)

print ("[*] coba akses kolum name")
print (dataset["name"])
