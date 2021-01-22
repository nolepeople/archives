import pandas as pd

print ("output json array")
json_data = pd.read_json("dataset/dataku.json")
print (json_data)

#gunakan lines=True untuk membaca json object
print ("output json object")
json_data = pd.read_json("dataset/dataku2.json",lines=True)
print (json_data)
