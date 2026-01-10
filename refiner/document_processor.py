from PyPDF2 import PdfReader
import docx

def process_documents(docs):
    extracted = []

    for doc in docs:
        if doc.endswith(".pdf"):
            reader = PdfReader(doc)
            text = " ".join(page.extract_text() for page in reader.pages)
        elif doc.endswith(".docx"):
            file = docx.Document(doc)
            text = " ".join(p.text for p in file.paragraphs)
        else:
            continue

        extracted.append({
            "requirement": text[:300],
            "priority": "High",
            "source": "Document"
        })

    return extracted
