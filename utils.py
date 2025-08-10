import os

def detect_file_type(path):
    if path.lower().endswith(".pdf"):
        return "pdf"
    elif path.lower().endswith(".docx"):
        return "docx"
    else:
        raise ValueError("Unsupported file type")
