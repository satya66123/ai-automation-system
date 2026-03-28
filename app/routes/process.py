from fastapi import APIRouter
from app.ai_engine import process_message

router = APIRouter()

@router.post("/process")
def process(data: dict):
    message = data.get("message")
    reply = process_message(message)
    return {"response": reply}