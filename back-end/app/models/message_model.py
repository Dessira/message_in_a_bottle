from datetime import datetime
from datetime import datetime

class MessageValidationError(Exception):
    """Custom exception for message validation errors."""
    pass

def validate_message(data):
    """Validates the message data."""
    required_fields = [
        "heading", "content", "owner", "read_status", 
        "reader", "country_created", "country_delivered"
    ]
    for field in required_fields:
        if field not in data:
            raise MessageValidationError(f"{field} is required.")

    if not isinstance(data["heading"], str) or not data["heading"].strip():
        raise MessageValidationError("Heading must be a non-empty string.")
    if not isinstance(data["content"], str) or not data["content"].strip():
        raise MessageValidationError("Content must be a non-empty string.")
    if not isinstance(data["owner"], str) or not data["owner"].strip():
        raise MessageValidationError("Owner must be a non-empty string.")
    if not isinstance(data["read_status"], bool):
        raise MessageValidationError("Read status must be a boolean.")
    if not isinstance(data["send_status"], bool):
        raise MessageValidationError("Read status must be a boolean.")
    if not isinstance(data["reader"], str) or not data["reader"].strip():
        raise MessageValidationError("Reader must be a non-empty string.")
    if not isinstance(data["country_created"], str) or not data["country_created"].strip():
        raise MessageValidationError("Country created must be a non-empty string.")
    if not isinstance(data["country_delivered"], str) or not data["country_delivered"].strip():
        raise MessageValidationError("Country delivered must be a non-empty string.")

def create_message_document(
    heading, content, owner, read_status, 
    reader, country_created, country_delivered
):
    data = {
        "heading": heading,
        "content": content,
        "owner": owner,
        "read_status": read_status,
        "reader": reader,
        "country_created": country_created,
        "country_delivered": country_delivered,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "sent_status": sent_status
    }
    validate_message(data)  # Validate data before returning
    return data

message_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "heading", "content", "owner_id", "read_status",
            "reader_id", "country_created", "country_delivered", "sent_status"
        ],
        "properties": {
            "heading": {"bsonType": "string", "description": "Heading is required and must be a string."},
            "content": {"bsonType": "string", "description": "Content is required and must be a string."},
            "owner_id": {"bsonType": "string", "description": "Owner is required and must be a string."},
            "read_status": {"bsonType": "bool", "description": "Read status is required and must be a boolean."},
            "reader_id": {"bsonType": "string", "description": "Reader is required and must be a string."},
            "country_created": {"bsonType": "string", "description": "Country created is required and must be a string."},
            "country_delivered": {"bsonType": "string", "description": "Country delivered is required and must be a string."},
            "created_at": {"bsonType": "date"},
            "updated_at": {"bsonType": "date"}
        }
    }
}


