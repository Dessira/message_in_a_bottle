from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.message_model import create_message_document, MessageValidationError
from app import mongo

message_routes = Blueprint("message_routes", __name__)

@message_routes.route("/", methods=["POST"])
def create_message():
    try:
        data = request.json
        message_document = create_message_document(**data)  # Pass data to model
        result = mongo.db.messages.insert_one(message_document)
        return jsonify({"message": "Message created successfully", "message_id": str(result.inserted_id)}), 201
    except MessageValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Failed to create message", "details": str(e)}), 500

@message_routes.route("/<message_id>", methods=["GET"])
def get_message(message_id):
    message = mongo.db.messages.find_one({"_id": ObjectId(message_id)})
    if message:
        message["_id"] = str(message["_id"])
        return jsonify(message), 200
    return jsonify({"error": "Message not found"}), 404
@message_routes.route("/<message_id>", methods=["POST"])
def send_message(message_id):
    # pick a user
    # pull message from db
    # update user id in the reader id
    pass
@message_routes.route("/<message_id>", methods=["PUT"])
def update_message(message_id):
    pass

@message_routes.route("/<message_id>", methods=["DELETE"])
def delete_message():
    # if id is owner remove user id
    # if id is reader remove owner id
    # if both ids are not existing then delete the document
    # send back succesfull message
    pass

