import pandas as pd

xlsx_d = pd.read_excel("dataset/absensi.xlsx",sheet_name="EKI-E")
print (xlsx_d.head())

