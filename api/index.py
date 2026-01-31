from fastapi import FastAPI, Header, HTTPException
from app.auth import verify_api_key
from app.detector import detect_scam
from app.agent import agent_reply
from app.memory import store_message

app = FastAPI()

@app.post("/honeypot/message")
async def handle_message(
    payload: dict,
    x_api_key: str = Header(None)
):
    # 🔐 API KEY CHECK
    verify_api_key(x_api_key)

    session_id = payload.get("sessionId")
    message = payload.get("message", {}).get("text", "")
    history = payload.get("conversationHistory", [])

    if not session_id or not message:
        raise HTTPException(status_code=400, detail="Invalid payload")

    store_message(session_id, message)

    scam_detected = detect_scam(message)

    if scam_detected:
        reply = agent_reply(session_id, history)
    else:
        reply = "Okay, noted."

    return {
        "scamDetected": scam_detected,
        "reply": reply,
        "sessionId": session_id
    }
