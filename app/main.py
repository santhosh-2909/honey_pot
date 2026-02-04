from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "HONEY_POT_SANTY"  # must match Vercel env value

@app.get("/")
def root(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "status": "Agentic Honeypot API is live",
        "message": "Validation endpoint working"
    }
