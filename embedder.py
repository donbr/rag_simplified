# embedder.py
from langchain.embeddings import OpenAIEmbeddings

def create_embeddings(texts):
    embedder = OpenAIEmbeddings()
    embeddings = embedder.embed_documents(texts)
    return embeddings