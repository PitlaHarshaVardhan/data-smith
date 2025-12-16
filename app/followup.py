def needs_followup(intent: str, text: str) -> bool:
    if intent == "unknown":
        return True
    if intent in ["summary", "sentiment", "code"] and len(text.strip()) < 40:
        return True
    return False
