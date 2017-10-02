from pymongo import MongoClient
import json
from flask import Flask, request
app = Flask(__name__)

# def courses():
#     course_dictionary = {"name": "Gym",
#                         "student_id": 4434,
#                         "students": ["Matthew", "Corey", "Ferdinand"]}
#     client = MongoClient('mongodb://localhost:27017/')
#     #In this line of code we created the database now we have to create the collection
#     database = client["student_courses"]
#     #What we are essentially doing here is that we are creating a collection within the database
#     subject_courses = database.subject_courses
#     subject_courses.insert_one(course_dictionary)
#     subject_courses.drop()

if __name__ == '__main__':
     course_dictionary = {"name": "Gym",
                         "student_id": 4434,
                         "students": ["Matthew", "Corey", "Ferdinand"]}
     client = MongoClient('mongodb://localhost:27017/')
     #In this line of code we created the database now we have to create the collection
     database = client.student_courses
     #What we are essentially doing here is that we are creating a collection within the database
     subject_courses = database.subject_courses
     subject_courses.drop()
     subject_courses.insert_one(course_dictionary)

    #  app.run()
