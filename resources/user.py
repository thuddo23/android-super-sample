from bson import ObjectId
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from schemas.user import UserSchema

blp = Blueprint("user", __name__, description="Operation with user/profile")


@blp.route("/get_user/<string:user_id>")
class GetUser(MethodView):

    @blp.response(200, UserSchema, description="return user info!")
    def get(self, user_id):
        user = db.user.find_one({"_id": ObjectId(user_id)}, {"_id": 0})

        if user:
            user_data = UserSchema().dump(user)
            return jsonify(user_data), 200
        else:
            return jsonify({'message': 'User not found'}), 404


@blp.route("/save_user")
class SaveUser(MethodView):

    @blp.arguments(UserSchema, description="save user to db!")
    def post(self, user_data):
        result = db.user.insert_one(user_data)

        if result.acknowledged:
            return {"message": "save user successfully"}
        else:
            return {"message": "save user failed!"}


@blp.route("/update_user")
class UpdateUser(MethodView):

    def put(self):
        return {"message": "Hello World!"}


@blp.route("/delete_user/<string:user_id>")
class DeleteUser(MethodView):

    def delete(self, user_id):
        result = db.user.delete_one({"_id": ObjectId(user_id)})

        if result.acknowledged:
            return {"message": "delete user successfully"}
        else:
            return {"message": "delete user failed!"}


@blp.route("/sign_out")
class SignOut(MethodView):

    def post(self):
        return {"message": "Hello World!"}
