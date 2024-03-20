# ollama_llm.py
from langchain.llms import Ollama

def generate_response(query, context_docs):
    llm = Ollama()
    prompt = f"Query: {query}\nContext:\n" + "\n".join(doc.page_content for doc in context_docs)
    response = llm(prompt)
    return response