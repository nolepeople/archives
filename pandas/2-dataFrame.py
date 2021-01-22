import pandas as pd


data = {
        "Nama":[
            "Natsuya",
            "Kenzomako",
            ],
        "Skill":[
            "Data Engineer",
            "Data Analyst",
            ],
        "github":[
            "nolepeople",
            "mako1337",
            ]
        }


df = pd.DataFrame(data)
print (df.head())

print ("\n\033[92mchange index label\033[97m")
df = pd.DataFrame(data,index=["satu","dua"])
print (df.head())



