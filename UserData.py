#Date:
#Authors: A.Suraj Kumar and Naveen N Prabhu
#Roll No: 181046037 and 181046017
#Data Retrival from GitHub on particular date


import requests
import random
import json
import csv
#from github import Github
#file_url = "http://data.gharchive.org/2018-09-17-18.json.gz"
count=0
user_data = []
for i in range(10):
	rand=random.randint(240000,250000)
	#print(rand)
	#username='suraj19'
	
	headers = {'Authorization': 'Authentication_token %s'}
	file_url1="https://api.github.com/user/"+str(rand)+":id"
	response1 = requests.get(file_url1, headers=headers)
	jsonToPython = response1.json()	#coverting json response to a python string
	#r= request.get(file_ural, stream = True)
	user_data.append(jsonToPython)
	#print(user_data)
	#columns=["login","id","public_repos","repos_url","followers","location","created_at"]
	user_list=[]
	#user_list.append(columns)
	for url in user_data:
		#print(url['repos_url'])
		'''repos_data=[]
		repo_link = url['repos_url']
		#file_url2="repo_link"user_data
		response2 = requests.get(repo_link, headers=headers)
		jsonToDict = response2.json()	#coverting json response to a python string
		repos_data.append(jsonToDict)'''
		temp=[]
		temp.append(url["login"])
		temp.append(url["id"])
		temp.append(url["public_repos"])
		temp.append(url["repos_url"])
		temp.append(url["followers"])
		temp.append(url["location"])
		temp.append(url["created_at"])
		user_list.append(temp)
		with open("UserData.csv","a",newline="") as f:
			writer=csv.writer(f)
			writer.writerows(user_list)
			#print('User Data is Downloaded')
	count+=1
	print('Number of user Data downloaded: ',count)
