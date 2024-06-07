from utils.utils import insert_data_signup
from sanic.response import json
import hashlib

async def hello(request):
    return json({"hello": "world"})

async def register(request):
    body = request.json
    first_name = body["first_name"]
    last_name = body["last_name"]
    password = hashlib.sha256(body['password'].encode()).hexdigest()
    email = body["email"]
    aadhar_number = body["aadhar_number"]

    if insert_data_signup(first_name, last_name, password, email, aadhar_number):
        return json({"status": 200, "message": "Data submitted successfully"})
    else:
        return json({"status": 400, "message": "Data submission failed"})

