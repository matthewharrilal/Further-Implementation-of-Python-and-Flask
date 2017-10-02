from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps
import json
from flask import Flask, request
app = Flask(__name__)

mongo = MongoClient('localhost', 27017)
# 3
app.db = mongo.develop_database
# 4
# api = Api(app)

@app.route('/student_courses',methods=["POST"])
def student_courses():
    course_dictionary = {"name": "Intro to Computer Science",
                        "student_id": 74834,
                        "students": ["Matthew", "Steven"]}
    # Request.json what it essentially does is that it allows us to serialize the data
# Making the database next we have to create a collection
    db = mongo["students_and_their_courses"]

    students_representation = db.students_representation
    students_representation.drop()
    students_representation.insert_one(course_dictionary)

    # course_dictionary = request.json
    json_representation = dumps(course_dictionary)
    return(json_representation, 200, None)

'''The reason that I strictly believe that the
databases are not being created withing mongo database is
because we are not running it in this function below'''

# @app.route('/matthew',methods=["GET","POST"])
# def student_courses():
#     student_course_dictionary = {"name": "Sociology",
#                                 "student_id": 432423,
#                                 "students": ["Matthew", "Alex", "Nick Swift"]}
#     json_casting = json.dumps(student_course_dictionary)
#     return (json_casting, 200, None)

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
