from utils.utils import insert_data_signup
from database.schemas import UserCreate
from sanic.response import json
from pydantic import ValidationError

async def hello(request):
    return json({"hello": "world"})

async def register(request):
    try:
        body = request.json

        user_data = UserCreate(**body)

        first_name = user_data.first_name
        last_name = user_data.last_name
        password = user_data.password
        email = user_data.email
        aadhar_number = user_data.aadhar_number

        if insert_data_signup(first_name, last_name, password, email, aadhar_number):
            return json({"status": 200, "message": "Data submitted successfully"})
        else:
            return json({"status": 400, "message": "Data submission failed"})
    except ValidationError as e:
        return json({"status": 400, "message": "Data validation failed", "errors": e.errors()})
    except Exception as e:
        return json({"status": 500, "message": "Data submission failed", "errors": str(e)})

async def login(request):
    pass

async def lender_login(request):
    pass

async def borrower_login(request):
    pass
