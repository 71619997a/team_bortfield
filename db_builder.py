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

print courses

sr.next()
for student in sr:
    print student
    id = int(student[2])
    age = int(student[1])
    name = int(student[0])
    myCourses = filter(lambda course: id == course[0], courses)
    # the filter gets every course of the student