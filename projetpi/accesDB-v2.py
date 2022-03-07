#!/usr/bin/env python
# scipt  accesBD.py
import pymongo, pprint
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
with MongoClient() as client:
	db = client.projetpi
	captures = db.captures
	for doc in captures.find({},{'_id':0, 'date': 1, 'source': 1, 'valeur': 1}):
		pprint.pprint(doc)
		print('-----------------------')

	print("----------------FIN-----------------------")
#serverStatusResult = db.captures()
#print (serverStatusResult)

#print(client.server_info())
#Verification
#print("List of databases after creating new one")
#print(client.list_database_names())

#db = client.projetpi
#    col = db["captures"]
#    for doc in col.find({},{'date' : 1, 'source' : 1, 'unite' : 1, 'valeur' : 1})
#    x = col.find({},{'date' : 1, 'source' : 1, 'unite' : 1, 'valeur' : 1})
#    pprint.pprint(x)
#x = col.find({},{'_id': 0, 'appliance': 1,
#				'rating': 1, 'company': 1})
##     for data in x:
##        print(data)
##        print("##########")




