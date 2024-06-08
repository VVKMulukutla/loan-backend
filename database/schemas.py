from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    confirmPassword: str
    gender: str


class UserLogin(BaseModel):
    username : str
    email : EmailStr
    password : str