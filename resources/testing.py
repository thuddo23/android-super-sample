from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

# from db import db
# from models import ItemModel
# from schemas import ItemSchema, ItemUpdateSchema

from flask_jwt_extended import jwt_required, get_jwt

blp = Blueprint("testings", __name__, description="Testing purpose, remove it soon")


@blp.route("/")
class Item(MethodView):

    def get(self):
        return {"message": "Hello World!"}
