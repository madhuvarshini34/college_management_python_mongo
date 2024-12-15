from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

# Initialize FastAPI app
app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['school']

class Student(BaseModel):
    name: str
    age: int
    grade: str

class Department(BaseModel):
    name: str
    degree: str
    hod_name: str

class Subject(BaseModel):
    name: str
    code: str
    credits: int

class Staff(BaseModel):
    name: str
    department: str
    experience: int

# Define routes to fetch data
@app.get("/", response_model=str)
def home():
    return "Welcome to the School API!"

@app.get("/students", response_model=List[Student])
def get_students():
    try:
        students = list(db.Student.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching students: {str(e)}")

@app.get("/departments", response_model=List[Department])
def get_departments():
    try:
        departments = list(db.Department.find({}, {"_id": 0}))
        return departments
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching departments: {str(e)}")

@app.get("/subjects", response_model=List[Subject])
def get_subjects():
    try:
        subjects = list(db.Subject.find({}, {"_id": 0}))
        return subjects
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching subjects: {str(e)}")

@app.get("/staff", response_model=List[Staff])
def get_staff():
    try:
        staffs = list(db.Staff.find({}, {"_id": 0}))
        return staffs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching staff: {str(e)}")

# Run the app on localhost:8080
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
