from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.user_model import create_user_document, UserValidationError
from app import mongo

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/", methods=["POST"])
def create_user():
    try:
        data = request.json
        user_document = create_user_document(**data)  # Pass data to model
        result = mongo.db.users.insert_one(user_document)
        return jsonify({"message": "User created successfully", "user_id": str(result.inserted_id)}), 201
    except UserValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error creating user", "details": str(e)}), 500

@user_routes.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_routes.route("/update_user", methods=["PUSH"])
def update_user():
    pass

@user_routes.route("/", methods=["DELETE"])
def delete_user():
    pass

