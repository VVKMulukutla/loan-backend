from sanic import Sanic
from sanic.response import json
from backend.utils.utils import insert_data

app = Sanic(__name__)


@app.route("/submit", methods=["POST"])
async def submit(request):
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    password = request.form.get("password")
    email = request.form.get("email")
    aadhar_number = request.form.get("aadhar_number")

    if(insert_data(first_name, last_name, password, email, aadhar_number)):
        return json({"status":200,"message": "Data submitted successfully"})
    else:
        return json({"status":400, "message": "Data submission failed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969, debug=True)