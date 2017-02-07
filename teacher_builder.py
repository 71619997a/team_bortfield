from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')
db = server.bortfielddb
teachercol = db.teachers
studentcol = db.students
tf = open('teachers.csv')
tr = csv.reader(tf)
tr.next()

for teacher in tr:
    code = teacher[0]
    name = teacher[1]
    pd = int(teacher[2])
    students = studentcol.find({'classes.name':code})
    studentids = [student['sid'] for student in students]
    teacherdata = {'name':name, 'period':pd, 'code':code, 'students':studentids}
    # print teacherdata
    teachercol.insert_one(teacherdata)
