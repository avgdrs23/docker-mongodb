#!/usr/bin/python3


# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient
#import sys
import csv 


try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database

db = conn.database
"""
Name =  (input("insert please name: "))
Age = (int(input("insert please your Age: ")))
City = (input("insert please your location: "))
"""
# Created or Switched to collection names: my_gfg_collection

collection = db.my_gfg_collection
"""
emp_rec = {
		"name":Name,
		"eid":Age,
		"location":City
		}

# Insert Data
rec_id = collection.insert_one(emp_rec)
#print("Data inserted with record ids",rec_id1," ",rec_id2)
"""
#print("Data inserted with record ids",rec_id)

with open('movies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
#   Skip the header line of the CSV file
    next(csv_reader)    
    line_count = 0   
    for row in csv_reader:
        name = row[8]
        desc = row[9]
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'name of movie {name}, Description: {desc}')
           # print(f'The data Number {line_count} is already  insert, {collection.insert_one(name)}, {collection.insert_one(desc)}') 
            line_count += 1
    print(f'Processed {line_count} lines.')
