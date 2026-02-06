from PyPDF2 import PdfReader
from docx import Document


def load_txt(file):
    return file.read().decode("utf-8")


def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def load_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])


def load_contract(file):
    if file.name.endswith(".txt"):
        return load_txt(file)
    elif file.name.endswith(".pdf"):
        return load_pdf(file)
    elif file.name.endswith(".docx"):
        return load_docx(file)
    else:
        return "Unsupported file format"
