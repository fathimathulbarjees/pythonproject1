from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from database import users_collection

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr  
    password: str

@app.get("/")
def home():
    return {"status": "success", "message": "API Running Successfully"}

@app.post("/register")
def register(user: User):
    users_collection.insert_one(user.model_dump())
    
    return {
        "status": "success",
        "message": "User Registered Successfully"
    }