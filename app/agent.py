# app/memory.py

from typing import Dict, List

# In-memory storage (resets on redeploy)
SESSION_STORE: Dict[str, List[str]] = {}


def store_message(session_id: str, message: dict):
    """
    Store user messages per session
    """
    if session_id not in SESSION_STORE:
        SESSION_STORE[session_id] = []

    SESSION_STORE[session_id].append(message.get("text", ""))


def get_history(session_id: str) -> List[str]:
    """
    Retrieve conversation history
    """
    return SESSION_STORE.get(session_id, [])
