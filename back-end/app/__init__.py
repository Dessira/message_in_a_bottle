from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def collection_exists(db, collection_name):
    """Check if a collection exists in the database."""
    return collection_name in db.list_collection_names()

def setup_mongo_validation(db):
    """Set up MongoDB JSON schema validation only if the collection doesn't exist."""
    from app.models.user_model import user_validator
    from app.models.message_model import message_validator

    if not collection_exists(db, "users"):
        db.create_collection("users", validator=user_validator)
    else:
        db.command({
            "collMod": "users",
            "validator": user_validator,
            "validationLevel": "strict"
        })

    if not collection_exists(db, "messages"):
        db.create_collection("messages", validator=message_validator)
    else:
        db.command({
            "collMod": "messages",
            "validator": message_validator,
            "validationLevel": "strict"
        })

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Configuration for MongoDB
    app.config["MONGO_URI"] = "mongodb://localhost:27017/bmessage"
    mongo.init_app(app)

    # Apply MongoDB validation
    with app.app_context():
        setup_mongo_validation(mongo.db)

    # Register Blueprints
    from app.routes.user_routes import user_routes
    from app.routes.message_routes import message_routes
    from app.routes.extra import extra_routes

    app.register_blueprint(user_routes, url_prefix="/users")
    app.register_blueprint(message_routes, url_prefix="/messages")
    app.register_blueprint(extra_routes, url_prefix="/")

    return app


