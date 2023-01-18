from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import request
import json

from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'thiya123'
app.config['MYSQL_DB'] = 'yahel'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:thiya123@localhost/yahel'

mysql = MySQL(app)
db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   age =db.Column(db.Integer)

   
   def __init__(self, name,age):
        self.name = name
        self.age = age
        
  
@app.route('/')
def show_all():
    res=[]
    for student in students.query.all():
        res.append({"id":student.id,"name":student.name,"age":student.age})
    return  (json.dumps(res))
   
 
@app.route('/new_student', methods = ['GET', 'POST'])
def new_student():
    request_data = request.get_json()
    name= request_data["name"]
    age = request_data["age"]
 
    newStudent= students(name,age)
    db.session.add (newStudent)
    db.session.commit()
    return "a new student add"

@app.route("/delete_student/<id>", methods=["DELETE"])
def delete_student(id):
    student = students.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return "student delete"

@app.route("/update_students/<id>", methods=["GET","PUT"])
def update_student(id):
    student = students.query.get(id)
    if student:
        student.name = request.json.get("name", student.name)
        student.age= request.json.get("age", student.age)
        stu_upd={"id":student.id,"name":student.name,"age":student.age}
        db.session.commit()
        return (json.dumps(stu_upd))
    else:
        return "error Student not found."



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)