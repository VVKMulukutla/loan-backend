from sanic import Sanic
from sanic.response import json
from utils.utils import insert_data
import json

app = Sanic(__name__)


@app.route("/hello", methods=["GET"])
async def hello(request):
    return json({"hello": "world"})

@app.route("/submit", methods=["POST"])
async def submit(request):

    body = json.loads(request.body.decode())

    print(body)

    first_name = body["first_name"]
    last_name = body["last_name"]
    password = body["password"]
    email = body["email"]
    aadhar_number = body["aadhar_number"]

    if(insert_data(first_name, last_name, password, email, aadhar_number)):
        return json({"status":200,"message": "Data submitted successfully"})
    else:
        return json({"status":400, "message": "Data submission failed"})

if __name__ == "__main__":
    app.run(host="localhost", port=6969, debug=True)