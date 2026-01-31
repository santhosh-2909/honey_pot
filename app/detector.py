# app/detector.py

SCAM_KEYWORDS = [
    "win",
    "prize",
    "lottery",
    "click",
    "free",
    "urgent",
    "verify",
    "bank",
    "password",
    "link"
]


def detect_scam(text: str) -> bool:
    """
    Very simple rule-based scam detector
    """
    text = text.lower()
    return any(keyword in text for keyword in SCAM_KEYWORDS)
