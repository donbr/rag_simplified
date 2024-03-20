# vector_db.py
from langchain.vectorstores import Chroma

def store_embeddings(embeddings, documents):
    vector_db = Chroma.from_documents(documents, embeddings)
    return vector_db

def retrieve_documents(query, vector_db):
    docs = vector_db.similarity_search(query)
    return docs