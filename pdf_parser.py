import PyPDF2
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image

def extract_text_from_pdf(file):
    
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if text.strip():  
            return text
    except Exception:
        pass 

    try:
        file.seek(0) 
        images = convert_from_bytes(file.read())
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"OCR failed: {e}"
