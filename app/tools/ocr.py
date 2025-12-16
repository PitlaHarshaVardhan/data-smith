import pytesseract
from PIL import Image
import io

def extract(file):
    img = Image.open(io.BytesIO(file.file.read()))

    data = pytesseract.image_to_data(
        img, output_type=pytesseract.Output.DICT
    )

    text = " ".join([w for w in data["text"] if w.strip()])

    confidences = [c for c in data["conf"] if isinstance(c, int) and c >= 0]

    avg_conf = round(sum(confidences) / len(confidences), 2) if confidences else 0.0

    return text.strip(), avg_conf
