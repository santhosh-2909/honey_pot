import os
from fastapi import HTTPException

def verify_api_key(x_api_key: str):
    expected_key = os.environ.get("X_API_KEY")

    if not x_api_key or x_api_key != expected_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
