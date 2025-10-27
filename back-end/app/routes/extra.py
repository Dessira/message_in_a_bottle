from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.message_model import create_message_document, MessageValidationError
from app import mongo

extra_routes = Blueprint("extra", __name__)

@extra_routes.route("/", methods=["GET"])
def Home():
    return "Hello world"