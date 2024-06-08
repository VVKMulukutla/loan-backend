from dotenv import load_dotenv
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

import os 

load_dotenv()

client = AsyncIOMotorClient(os.getenv("DATABASE_URI"))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["loan-users"]
collection = db["loan-users-collection"]
