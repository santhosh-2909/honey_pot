from fastapi import FastAPI, Depends
from app.auth import verify_api_key
from app.detector import detect_scam
from app.agent import agent_reply
from app.memory import store_message

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Agentic Honeypot API is live"}

@app.post("/honeypot/message")
def handle_message(payload: dict, api_key: str = Depends(verify_api_key)):
    session_id = payload["sessionId"]
    message = payload["message"]["text"]
    history = payload.get("conversationHistory", [])

    store_message(session_id, message)

    if detect_scam(message):
        reply = agent_reply(session_id, history)
    else:
        reply = "Okay, noted."

    return {"status": "success", "reply": reply}
