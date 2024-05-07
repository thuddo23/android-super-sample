from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import redirect, url_for, session

from db import db
# from models import ItemModel
# from schemas import ItemSchema, ItemUpdateSchema

from flask_jwt_extended import jwt_required, get_jwt

from common.token_validation import validate_token

from schemas.token import TokenSchema

blp = Blueprint("authorization", __name__, description="Operation with user/profile")

@blp.route("/token_verification")
class Token(MethodView):

    @blp.arguments(TokenSchema)
    def post(self, token):
        if "token_type" in token and "token_id" in token and validate_token(token["token_type"], token["token_id"]):
            session["name"] = "thuandohusk65"
            db.user.insert_one({
                "name": session["name"],
                "age": 22
            })
            return redirect("/authorized")
        return redirect("/unauthorized")

@blp.route("/unauthorized")
class UnAuthorized(MethodView):

    def get(self):
        abort(
            401,
            message="Not Authorized"
        )

@blp.route("/authorized")
class Authorized(MethodView):

    def get(self):
        if session.get("name"):
            return {"success": "true",
                    "user_name": session.get("name")}
        return redirect("/unauthorized")
