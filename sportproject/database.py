from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")

# db = client["user_database"]

# users_collection = db["users"]

# print("Successfully!")



import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["user_database"]

users_collection = db["users"]

print("MongoDB Atlas Connected Successfully!")