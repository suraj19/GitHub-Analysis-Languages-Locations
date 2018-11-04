import requests
import random
import json
import csv
import pandas as pd
df=pd.read_csv("file.csv",encoding="cp1252")
repos_url=df.iloc[1:,3]
for url in repos_url:
    #print(url)
#token1='9d98deacd0b4b3b3efdfb254c6af5c931ec237c5'
#token2='808fd391c6908d19ceca268a311f3cb53a92b4e0'
#Naveen's token: '19d3613f87d6be4b31d6480ac9aa6692aa47cd47'
#Naveen's new token: '8103f0da6d0cd4dda76ba3960fd635ad82a74e34'
#Vivek's Token: '0d494f03e8aeab180598b9f6cfd6c53ee56b9190'
#Suraj New Token: 'bcda4a9669f4c0bba564f7d8d90bdbe6be90ef3d'
#Noopur's Token:'3e24f3ad2a447fddd55bc549718c74f030599222'
#Ramy's Token: 'c45709566c371d0d77a4a121857d3813fec5ae45'
    headers = {'Authorization': '19d3613f87d6be4b31d6480ac9aa6692aa47cd47 %s'}
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
