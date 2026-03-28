from app.services.classifier import classify_message
from app.services.responder import generate_response

def process_message(message: str):
    category = classify_message(message)
    response = generate_response(category)
    return response