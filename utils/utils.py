import sys
sys.path.append('..')

import hashlib
from backend.database.config import collection

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def insert_data_signup(first_name, last_name, password, email, aadhar_number):
        try:
            hashed_password = hash_password(password)
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": hashed_password,
                "aadhar_number": aadhar_number
            }
            collection.insert_one(user_data)
            return True
        except Exception as e:
            print(f"Error inserting data: {e}")
            return False

