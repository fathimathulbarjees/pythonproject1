

from django.db import models

from pydantic import BaseModel, EmailStr




class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    username: str
    password: str
