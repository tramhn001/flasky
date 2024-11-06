from flask import Blueprint, request
from app.models.caretaker import Caretaker
from .route_utilities import validate_model, create_model, get_models_with_filters
from app.models.cat import Cat
from ..db import db

bp = Blueprint("caretakers_bp", __name__, url_prefix="/caretakers")

@bp.post("")
def create_caretaker():
    request_body = request.get_json()
    return create_model(Caretaker, request_body)

@bp.get("")
def get_all_caretakers():
    return get_models_with_filters(Caretaker, request.args)

@bp.post("/<caretaker_id>/cats")
def create_cat_with_caretaker_id(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)

    request_body = request.get_json()
    request_body["caretaker_id"] = caretaker.id

    return create_model(Cat, request_body)

@bp.get("/<caretaker_id>/cats")
def get_cats_by_caretaker(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    response = [cat.to_dict() for cat in caretaker.cats]
    return response
