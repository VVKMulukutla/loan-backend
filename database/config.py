from dotenv import load_dotenv
from pymongo import MongoClient
import os 

load_dotenv()

client = MongoClient(os.getenv("DATABASE_URI"))

db = client["user"]
collection = db["user-collection"]
