import sys
sys.path.append('..')

import hashlib
from backend.database.config import collection

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def insert_data_signup(firstname, lastname, password, confirmPassword, email, gender):
        try:
            hashed_password = hash_password(password)
            hashed_confirmPassword = hash_password(confirmPassword)
            user_data = {
                "first_name": firstname,
                "last_name": lastname,
                "email": email,
                "password": hashed_password,
                "confirmPassword": hashed_confirmPassword,
                "gender": gender
            }
            collection.insert_one(user_data)
            return True
        except Exception as e:
            print(f"Error inserting data: {e}")
            return False

def check_login(username, email, password):
    try:
        hashed_password = hash_password(password)
        user = collection.find_one({"email": email, "password": hashed_password})
        if user:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking login: {e}")
        return False

def kyc_function_helper():
    pass