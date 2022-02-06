#!/usr/bin/python3


# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")
      
# database
db = conn.database

# Created or Switched to collection names: my_gfg_collection

collection = db.my_gfg_collection

# Printing the data inserted
cursor = collection.find()
for record in cursor:
	print(record)


