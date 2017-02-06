from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')  # '149.89.150.100')
db = server.bortfielddb
collection = db.students

###DISPLAY CASE###

print("Name -- Student ID -- Average")
print("_____________________________\n")
for student in collection.find():
    classes = student["classes"]
    gsum = 0;
    counter = 0;
    for a in classes:
        gsum += int(a["mark"])
        counter += 1
    average = gsum / counter
    print(student["name"] + " -- " + str(student["sid"]) + " -- " + str(average))



