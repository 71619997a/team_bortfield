from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
db = server.bortfielddb
collection = db.students

sf = open('peeps.csv')
cf = open('courses.csv')
sr = csv.reader(sf)
cr = csv.reader(cf)
cr.next()
sr.next()
for student in sr:
    print student

