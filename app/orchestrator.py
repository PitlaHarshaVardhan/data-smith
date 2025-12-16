from app.intent import detect_intent
from app.followup import needs_followup
from app.tools import ocr, pdf_parser, audio_stt
from app.tools import summarizer, sentiment, code_analyzer, youtube

def run_agent(input_text, file=None):
    logs = []
    extracted_text = ""

    # 1. Content Extraction
    if file:
        name = file.filename.lower()
        if name.endswith((".png", ".jpg", ".jpeg")):
            extracted_text, conf = ocr.extract(file)
            logs.append(f"OCR confidence: {conf}")
        elif name.endswith(".pdf"):
            extracted_text = pdf_parser.extract(file)
            logs.append("PDF text extracted")
        elif name.endswith((".mp3", ".wav", ".m4a")):
            extracted_text = audio_stt.transcribe(file)
            logs.append("Audio transcribed")

    combined = input_text + "\n" + extracted_text

    # 2. Intent Detection
    intent = detect_intent(combined)
    logs.append(f"Detected intent: {intent}")

    # 3. Mandatory Follow-Up
    if needs_followup(intent, combined):
        return {
            "followup": "What do you want me to do with this content?",
            "extracted_text": extracted_text,
            "logs": logs
        }

    # 4. Tool Routing
    if intent == "youtube":
        result = youtube.fetch(combined)
    elif intent == "summary":
        content = extracted_text if extracted_text.strip() else input_text
        result = summarizer.run(content)

    elif intent == "sentiment":
        result = sentiment.run(extracted_text)
    elif intent == "code":
        result = code_analyzer.run(extracted_text)
    else:
        result = summarizer.run(combined)

    return {
        "extracted_text": extracted_text,
        "result": result,
        "logs": logs
    }
