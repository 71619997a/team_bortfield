from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')  # '149.89.150.100')
db = server.bortfielddb
collection = db.students

sf = open('peeps.csv')
cf = open('courses.csv')
sr = csv.reader(sf)
cr = csv.reader(cf)
cr.next()  # skip column descriptions
# we want a list of courses, [[id, {name: x, mark: y}], ...]
# this will make it easier to pick a student's courses
courses = []
for course in cr:
    entry = [int(course[2])]  # id
    cinfo = {'name': course[0], 'mark': course[1]}
    entry.append(cinfo)
    courses.append(entry)

# print "courses\n" 
# print courses
# print "----------\n"

sr.next()
documents = []
for student in sr:
    docdict = {};
    id = int(student[2])
    age = int(student[1])
    name = student[0]
    docdict["name"] = name
    docdict["age"] = age
    #docdict["sid"] = id
    myCourses = filter(lambda course: id == course[0], courses)
    # the filter gets every course of the student
    classes = []
    for aclass in myCourses:
        classes.append(aclass[1])
    docdict["classes"] = classes
    documents.append(docdict)

result = collection.insert_many(documents)

for doc in collection.find():
    print(doc)
    print "\n\n"
