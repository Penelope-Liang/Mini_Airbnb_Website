from db import db
from models.user import UserModel
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from resources.tools.register import register_format_checker, register_saving
from resources.tools.exceptions import InvaildRegister


blp = Blueprint("register", __name__, description="saving register")


@blp.route("/register")
class UserRegister(MethodView):

    def get(self):
        return "yes"

    def post(self):
        user_data = request.get_json()
        print(user_data)

        try:
            register_format_checker(user_data)
            user_data = register_saving(user_data)
        except InvaildRegister as IR:
            return IR.message, 404

        print(user_data)

        userM = UserModel(**user_data)
        print(userM)
        db.session.add(userM)
        db.session.commit()
        return "You have registered, well done!", 200
