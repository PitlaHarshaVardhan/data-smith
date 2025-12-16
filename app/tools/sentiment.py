def run(text):
    positive_words = ["good", "great", "happy", "excellent", "love"]

    score = sum(
        1 for w in text.lower().split() if w in positive_words
    )

    if score > 0:
        label = "Positive"
        confidence = 0.7
    else:
        label = "Neutral"
        confidence = 0.5

    return {
        "label": label,
        "confidence": confidence,
        "justification": "Rule-based sentiment detection"
    }
