from utils.utils import *
from database.schemas import UserCreate, UserLogin
from sanic.response import json
from pydantic import ValidationError

async def hello(request):
    return json({"hello": "world"})

async def register(request):
    try:
        body = request.json

        user_data = UserCreate(**body)

        firstname = user_data.firstname
        lastname = user_data.lastname
        password = user_data.password
        confirmPassword = user_data.confirmPassword
        email = user_data.email
        gender = user_data.gender

        if insert_data_signup(firstname, lastname, password, confirmPassword, email, gender):
            return json({"status": 200, "message": "Data submitted successfully"})
        else:
            return json({"status": 400, "message": "Data submission failed"})
    except ValidationError as e:
        return json({"status": 400, "message": "Data validation failed", "errors": e.errors()})
    except Exception as e:
        return json({"status": 500, "message": "Data submission failed", "errors": str(e)})

async def login(request):
    try:
        body = request.json

        user_login = UserLogin(**body)

        username = user_login.username
        email = user_login.email
        password = user_login.password

        if(check_login(username, email, password)):
            return json({"status": 200, "message": "Login successful"})
        else:
            return json({"status": 400, "message": "Login failed"})
    except ValidationError as e:
        return json({"status": 400, "message": "Data validation failed", "errors": e.errors()})
    except Exception as e:
        return json({"status": 500, "message": "Login failed", "errors": str(e)})

async def lender_login(request):
    pass

async def borrower_login(request):
    pass
