from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "HACKATHON_SECRET_KEY"

@app.get("/")
def root():
    return {"status": "Agentic Honeypot API is live"}

@app.post("/honeypot/message")
def honeypot_message(
    payload: dict,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    text = payload["message"]["text"]

    scam_detected = any(word in text.lower() for word in ["prize", "click", "win", "otp"])

    return {
        "scam_detected": scam_detected,
        "agent_reply": "Thanks, I will check and get back to you.",
        "extracted_intel": {
            "urls": [],
            "upi_ids": [],
            "bank_accounts": []
        }
    }
