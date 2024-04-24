print("This is my_api.py file.")

from flask import Flask,jsonify,request
import json

app=Flask(__name__) #create Flask appilcation in current file (refrenced in __name__)

##Create a simple api
##function(python,java)=Link-Button-Response
##Button->request a link->triggers a function ...
##API->Link->function->request/input->response/output

##Api No. 1
@app.route("/welcome")
def welcome_func():
    return "Welcome User!"

@app.route("/")
@app.route("/home")
def home_func():
    return "Home Page!"

##Create a Student catalog using Flask
#Data related to students
#APIs related to students

# db=[{"id":1,"name":"Student1","Address":"France"},
#     {"id":2,"name":"Student2","Address":"India"}]

def save_data(db):
    with open("student_db.json","w") as db_file:
        json.dump(db,db_file)

def read_db(db_path): #db_path="student_db.json"
    with open(db_path,"r") as db_file:
        db=json.load(db_file)
    return db

## GET API

@app.route("/get_students",methods=["GET"])
def read_students():
    db=read_db("student_db.json")
    return db

#Reads data of specific student
@app.route("/get_std_by_id/<int:std_id>",methods=["GET"])
def read_std_by_id(std_id):
    db=read_db("student_db.json")
    db=list(db)#just to be safe
    for std in db:
        if std["id"]==std_id:
            return std
    return "Student with given id not found!"

##POST API to create data on server

@app.route("/add_student",methods=["POST"])
def add_student_in_db():
    db=read_db("student_db.json")
    db=list(db)
    new_std=request.get_json()
    db.append(new_std)
    save_data(db)
    return "New Student Added Successfully!"

##PUT API for update
@app.route("/update_std",methods=["PUT"])
def update_std():
    db=read_db("student_db.json")
    db=list(db)
    new_std_data=request.get_json()
    for std in db:
        if std["id"]==new_std_data["id"]:
            std["name"]=new_std_data["name"]
            std["Address"]=new_std_data["Address"]
            save_data(db)
            return "Student data updated successfully."
    return "Student with given id not found!"

##DELETE to delete data
@app.route("/delete_user",methods=["DELETE"])
def delete_std():
    db=read_db("student_db.json")
    db=list(db)
    std_del_id=request.get_json()

    del_index=None
    for i in range(len(db)):
        if db[i]["id"]==std_del_id["id"]:
            del_index=i

    if del_index==None:
        return "Student with given id not found"

    del db[del_index]
    save_data(db)
    return "Student deleted successfully!"

if __name__=="__main__":
    app.run(debug=True)#Automatically reolads when changes made
