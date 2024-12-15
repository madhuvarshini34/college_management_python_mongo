from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create (or switch to) the database
db = client['school']

print("Connected to MongoDB!")
