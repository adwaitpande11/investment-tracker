from flask import request, jsonify

from application import app
from application.user_service import UserService


@app.route("/")
def test():
    return "It works!"


@app.route("/save-user", methods=['POST'])
def save_user():
    service_result = UserService().save_user(request.json)
    if service_result:
        return jsonify(str(service_result))
    else:
        return '0'
