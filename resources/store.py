import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from resources.schemas import StoreSchema

from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import StoreModel



blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
    @blp.response(200, StoreSchema)
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store successfully deleted"}


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):

        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with the name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the store")

        return store