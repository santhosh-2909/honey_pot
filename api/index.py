from fastapi import FastAPI, Header, HTTPException
import os

app = FastAPI(title="Agentic Honeypot API")

API_KEY = os.getenv("HONEY_API_KEY")

@app.post("/honeypot/message")
async def handle_message(
    payload: dict,
    x_api_key: str = Header(None)
):
    # 🔐 API KEY CHECK
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    session_id = payload.get("sessionId")
    message = payload.get("message", {}).get("text", "")

    # 🧠 Simple scam detection (extend later)
    scam_keywords = ["urgent", "verify", "account", "blocked", "prize", "won"]
    scam_detected = any(word in message.lower() for word in scam_keywords)

    if scam_detected:
        reply = "Why are you asking for this? Can you explain more?"
    else:
        reply = "Okay, noted."

    return {
        "status": "success",
        "scamDetected": scam_detected,
        "reply": reply
    }
