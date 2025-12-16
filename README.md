Agentic Multimodal AI Application
Overview

This project is an agentic, multimodal AI system built using FastAPI.
The application accepts Text, Images, PDFs, and Audio files, extracts their content using appropriate tools, understands the user’s intent, and autonomously executes the correct task.

A mandatory follow-up mechanism ensures the agent never guesses when the user’s goal is unclear.

All outputs are text-only, with explainable logs returned for every execution.

Key Features

✅ Multimodal input support (Text, Image, PDF, Audio)

✅ Deterministic intent detection (rule-based)

✅ Tool-first orchestration (LLM not overused)

✅ Mandatory follow-up question enforcement

✅ Explainable execution logs

✅ Production-ready FastAPI architecture

✅ Clean, minimal UI

✅ Automated test cases

Supported Inputs & Processing
Input Type	Processing Method
Text	Direct analysis
Image (PNG/JPG)	OCR using Tesseract
PDF	Text parsing using pdfplumber
Audio	Speech-to-text (pluggable Whisper module)
YouTube URL	Transcript fetch with fallback
Agent Behavior
1. Content Extraction

Images → OCR + confidence score

PDFs → Text extraction (OCR fallback mentioned)

Audio → Transcription module

YouTube URLs → Transcript fetching

2. Intent Understanding

The agent detects intent using rule-based logic:

Summary

Sentiment analysis

Code explanation

YouTube transcript

Unknown intent

This ensures predictable, explainable behavior.

3. Mandatory Follow-Up Rule (Core Requirement)

If:

The intent is unclear

OR multiple tasks are equally possible

OR insufficient content is provided

➡️ The agent asks a follow-up question and stops execution

Example:

{
  "followup": "What do you want me to do with this content?"
}


This prevents hallucination or incorrect task execution.

Tasks Supported
✔ Text / Image / PDF Extraction

Returns cleaned extracted text

Includes OCR confidence (for images)

✔ Summarization

Outputs:

1-line summary

3 bullet points

5-sentence summary

✔ Sentiment Analysis

Outputs:

Sentiment label

Confidence score

One-line justification

✔ Code Explanation

Explains what the code does

Highlights potential issues

Mentions time complexity (high-level)

✔ Audio Transcription + Summary

Audio → text (placeholder, Whisper-ready)

Same summarization formats applied

✔ Conversational Answers

Friendly responses for general queries

Architecture
UI (HTML)
   |
FastAPI API Layer
   |
Agent Orchestrator
   |
Intent Detection (Rule-Based)
   |
Tool Router
   |
Task Executors
   |
Text-only Output + Logs

Design Principles

Tool-first execution

Minimal LLM usage

Clear separation of concerns

Easy extensibility

Production-oriented structure

Technology Stack

Backend: FastAPI

OCR: Tesseract (pytesseract)

PDF Parsing: pdfplumber

YouTube: youtube-transcript-api

Testing: pytest

UI: HTML + JavaScript

Language: Python 3.10+

Project Structure
agentic-ai-app/
│
├── app/
│   ├── main.py
│   ├── orchestrator.py
│   ├── intent.py
│   ├── followup.py
│   └── tools/
│
├── ui/
│   └── index.html
│
├── tests/
│   └── test_agent.py
│
├── conftest.py
├── requirements.txt
└── README.md

How to Run
1. Create virtual environment
python -m venv venv

2. Activate

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Start the server
uvicorn app.main:app --reload

5. Open browser

UI: http://127.0.0.1:8000/

API Docs: http://127.0.0.1:8000/docs

Running Tests
pytest


Expected output:

1 passed

Sample Test Scenarios
1️⃣ Audio Lecture

Upload audio

Agent transcribes

Returns 1-line + bullets + 5-sentence summary

2️⃣ PDF with Meeting Notes

Prompt:

What are the action items?


Agent:

Extracts text

Identifies relevant points

3️⃣ Image with Code

Prompt:

Explain this code


Agent:

OCRs image

Detects code

Explains logic and complexity

Robustness & Error Handling

Unsupported files handled safely

Missing transcripts return fallback messages

Empty inputs trigger follow-up questions

Partial extraction does not crash the system

Explainability

Each response includes:

Detected intent

Tools used

Execution logs

This improves transparency and debuggability.

Bonus Considerations

Planner–Executor separation possible

Whisper STT can be plugged easily

Cost estimation layer can be added before execution

Final Notes

This project emphasizes:

Engineering discipline

Autonomous agent behavior

Explainability

Minimal dependency on LLMs

Designed to be scalable, testable, and production-ready.
