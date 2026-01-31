# app/main.py

from fastapi import FastAPI, Depends
from app.auth import verify_api_key
from app.detector import detect_scam
from app.agent import agent_reply
from app.memory import store_message

app = FastAPI(title="Agentic Honeypot API")


@app.get("/")
def root():
    return {"status": "Agentic Honeypot API is live"}


@app.post("/honeypot/message")
def handle_message(payload: dict, api_key: str = Depends(verify_api_key)):
    session_id = payload.get("sessionId")
    message = payload.get("message", {})
    history = payload.get("conversationHistory", [])

    store_message(session_id, message)

    is_scam = detect_scam(message.get("text", ""))

    if is_scam:
        reply = agent_reply(session_id, history)
    else:
        reply = "Message received. Thank you."

    return {
        "status": "success",
        "scamDetected": is_scam,
        "reply": reply
    }
