from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from app.orchestrator import run_agent
import os

app = FastAPI(title="Agentic AI System")

@app.get("/", response_class=HTMLResponse)
def home():
    file_path = os.path.join("ui", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

@app.post("/process")
async def process(text: str = Form(""), file: UploadFile = None):
    return run_agent(text, file)
