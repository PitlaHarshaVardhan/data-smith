def detect_intent(text: str) -> str:
    t = text.lower()

    if "youtube.com" in t or "youtu.be" in t:
        return "youtube"

    if "explain" in t or "code" in t or "debug" in t:
        return "code"

    if "sentiment" in t:
        return "sentiment"

    if "summary" in t or "summarize" in t:
        return "summary"

    return "unknown"
