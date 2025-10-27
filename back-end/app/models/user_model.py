from datetime import datetime
from datetime import datetime

class UserValidationError(Exception):
    """Custom exception for user validation errors."""
    pass

def validate_user(data):
    """Validates the user data."""
    required_fields = ["first_name", "last_name", "email", "password", "username", "age"]
    for field in required_fields:
        if field not in data:
            raise UserValidationError(f"{field} is required.")

    if not isinstance(data["first_name"], str) or not data["first_name"].strip():
        raise UserValidationError("First name must be a non-empty string.")
    if not isinstance(data["last_name"], str) or not data["last_name"].strip():
        raise UserValidationError("Last name must be a non-empty string.")
    if not isinstance(data["email"], str) or "@" not in data["email"]:
        raise UserValidationError("Email must be a valid email address.")
    if not isinstance(data["password"], str) or len(data["password"]) < 6:
        raise UserValidationError("Password must be at least 6 characters long.")
    if not isinstance(data["username"], str) or not data["username"].strip():
        raise UserValidationError("Username must be a non-empty string.")
    if not isinstance(data["age"], int) or data["age"] <= 0:
        raise UserValidationError("Age must be a positive integer.")

    # Optional field: user_country
    if "user_country" in data and not (isinstance(data["user_country"], str) or data["user_country"] is None):
        raise UserValidationError("User country must be a string or null.")

def create_user_document(first_name, last_name, email, password, username, age, user_country=None):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "username": username,
        "age": age,
        "user_country": user_country,  # This field is optional
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    validate_user(data)  # Validate data before returning
    return data

user_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["first_name", "last_name", "email", "password", "username", "age"],
        "properties": {
            "first_name": {"bsonType": "string", "description": "First name is required and must be a string."},
            "last_name": {"bsonType": "string", "description": "Last name is required and must be a string."},
            "email": {
                "bsonType": "string",
                "pattern": "^.+@.+$",
                "description": "Email is required and must be a valid email address."
            },
            "password": {"bsonType": "string", "description": "Password is required and must be a string."},
            "username": {"bsonType": "string", "description": "Username is required and must be a string."},
            "age": {"bsonType": "int", "minimum": 1, "description": "Age is required and must be a positive integer."},
            "user_country": {"bsonType": ["string", "null"], "description": "User country must be a string or null."},
            "created_at": {"bsonType": "date"},
            "updated_at": {"bsonType": "date"}
        }
    }
}

