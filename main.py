from sanic import Sanic
from sanic.response import json
from routes.settings import *


app = Sanic(__name__)


app.add_route(hello, "/hello", methods=["GET"])


app.add_route(register, '/register', methods=["POST"])
app.add_route(login, '/login', methods=["POST"])
app.add_route(lender_login, '/lender_login', methods=["POST"])
app.add_route(borrower_login, '/borrower_login', methods=["POST"])



if __name__ == "__main__":
    app.run(host="localhost", port=6969, debug=True)
