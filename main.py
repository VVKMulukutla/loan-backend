from sanic import Sanic
from sanic.response import json
from routes.settings import *


app = Sanic(__name__)


app.route(hello, "/hello", methods=["GET"])


app.add_route(register, '/register', methods=["POST"])

if __name__ == "__main__":
    app.run(host="localhost", port=6969, debug=True)
