from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['school']

# Insert data into collections
print("Inserting data into collections...")

# Insert Students
students_data = [
    {"name": "Madhu", "age": 20, "grade": "A"},
    {"name": "Jeeva", "age": 21, "grade": "B"}
]
db.Student.insert_many(students_data)

# Insert Departments
departments_data = [
    {"name": "Computer Science", "degree": "B.Sc", "hod_name": "Dr. P.M.Gomathi"},
    {"name": "Commerce", "degree": "B.COM", "hod_name": "Dr. S.Vijay"}
]
db.Department.insert_many(departments_data)

# Insert Subjects
subjects_data = [
    {"name": "Mathematics", "code": "M101", "credits": 4},
    {"name": "Physics", "code": "P101", "credits": 3}
]
db.Subject.insert_many(subjects_data)

# Insert Staff
staff_data = [
    {"name": "Dr. Rajesh", "department": "Physics", "experience": 10},
    {"name": "Ms. Priya", "department": "Mathematics", "experience": 8}
]
db.Staff.insert_many(staff_data)
