import pdfplumber

def extract(file):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text.strip()
