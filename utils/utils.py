import sys
sys.path.append('..')

from backend.database.config import collection

def insert_data(first_name, last_name, password, email, aadhar_number):
        data = {
            "FirstName": first_name,
            "LastName": last_name,
            "Password": password,
            "Email": email,
            "AadharNumber": aadhar_number
        }
        res = collection.insert_one(data)

        return (res != None) 
    


# Check if the connection is successful
try:
    # Perform a simple query to verify the connection
    result = collection.find_one()
    if result is not None:
        print("Connection to MongoDB successful")
    else:
        print("Connection to MongoDB failed")
except Exception as e:
    print("Connection to MongoDB failed:", str(e))
