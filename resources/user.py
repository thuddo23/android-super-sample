from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

# from db import db
# from models import ItemModel
# from schemas import ItemSchema, ItemUpdateSchema

from flask_jwt_extended import jwt_required, get_jwt

blp = Blueprint("user", __name__, description="Operation with user/profile")

@blp.route("/get_user")
class GetUser(MethodView):

    def get(self):
        return {"message": "Hello World!"}


@blp.route("/update_user")
class UpdateUser(MethodView):

    def put(self):
        return {"message": "Hello World!"}

@blp.route("/delete_user")
class DeleteUser(MethodView):

    def delete(self):
        return {"message": "Hello World!"}

@blp.route("/sign_out")
class SignOut(MethodView):

    def post(self):
        return {"message": "Hello World!"}