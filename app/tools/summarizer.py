def run(text):
    sentences = [s for s in text.split(".") if s.strip()]
    return {
        "one_line": sentences[0] if sentences else "",
        "bullets": sentences[:3],
        "five_sentence_summary": ". ".join(sentences[:5])
    }
