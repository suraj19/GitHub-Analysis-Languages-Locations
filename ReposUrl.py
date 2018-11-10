import requests
import random
import json
import csv
import pandas as pd
df=pd.read_csv("file.csv",encoding="cp1252")
repos_url=df.iloc[1:,3]
for url in repos_url:
    #print(url)

    headers = {'Authorization': 'Authentication_token %s'}
    response2 = requests.get(url, headers=headers)
    jsonToDict = response2.json()	#coverting json response to a python string
    repos_data=[]
    repos_data.append(jsonToDict)
    columns=["Login","Id","created_at","Language","Size"]
    Repos_list=[]
    Repos_list.append(columns)
    #print(repos_data)
    for repo in jsonToDict:
        temp=[]
        temp.append(repo['owner']['login'])
        temp.append(repo['owner']['id'])#at a time we cant append 2 key values to a list
        temp.append(repo['created_at'])
        temp.append(repo['language'])
        temp.append(repo['size'])
        Repos_list.append(temp)
        with open("New_Repos_Data.csv","a",newline="") as f:
            writer=csv.writer(f)
            writer.writerows(Repos_list)
            print('User Data is Downloaded')
