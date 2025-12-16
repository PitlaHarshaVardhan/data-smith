from app.intent import detect_intent

def test_detect_summary():
    assert detect_intent("Please summarize this") == "summary"
