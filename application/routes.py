from application import app
from flask import request


@app.route("/")
def test():
    return "It works!"


@app.route("/save-user", methods=['POST'])
def save_user():
    return request.json
