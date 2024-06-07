import sys
sys.path.append('..')

from backend.database.config import collection

def insert_data_signup(first_name, last_name, password, email, aadhar_number):
        data = {
            "FirstName": first_name,
            "LastName": last_name,
            "Password": password,
            "Email": email,
            "AadharNumber": aadhar_number
        }
        res = collection.insert_one(data)

        return (res != None) 
    

