# document_loader.py
import os
import json
import pypdf2
import docx

def load_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            with open(os.path.join(directory, filename), "rb") as file:
                pdf_reader = pypdf2.PdfReader(file)
                text = " ".join(page.extract_text() for page in pdf_reader.pages)
                documents.append({"text": text, "metadata": {"source": filename}})
        elif filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                documents.append({"text": data["text"], "metadata": data["metadata"]})
        elif filename.endswith(".docx"):
            doc = docx.Document(os.path.join(directory, filename))
            text = " ".join(paragraph.text for paragraph in doc.paragraphs)
            documents.append({"text": text, "metadata": {"source": filename}})
    return documents