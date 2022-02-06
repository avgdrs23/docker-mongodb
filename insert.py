#!/usr/bin/python3


# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient
import sys

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database

db = conn.database
Name =  (input("insert please name: "))
Age = (int(input("insert please your Age: ")))

City = (input("insert please your location: "))
# Created or Switched to collection names: my_gfg_collection

collection = db.my_gfg_collection

emp_rec = {
		"name":Name,
		"eid":Age,
		"location":City
		}

# Insert Data
rec_id1 = collection.insert_one(emp_rec)
#print("Data inserted with record ids",rec_id1," ",rec_id2)

print("Data inserted with record ids",rec_id1)

