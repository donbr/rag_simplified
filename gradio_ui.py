# gradio_ui.py
import gradio as gr
from document_loader import load_documents
from web_search import search_web
from embedder import create_embeddings
from vector_db import store_embeddings, retrieve_documents
from ollama_llm import generate_response

def process_query(query, retrieval_type):
    if retrieval_type == "Document":
        documents = load_documents("path/to/documents")
        embeddings = create_embeddings([doc["text"] for doc in documents])
        vector_db = store_embeddings(embeddings, documents)
        context_docs = retrieve_documents(query, vector_db)
    else:
        search_results = search_web(query)
        context_docs = [{"page_content": result} for result in search_results]

    response = generate_response(query, context_docs)
    return response

input_query = gr.Textbox(label="Enter your query")
input_retrieval_type = gr.Radio(["Document", "Web Search"], label="Retrieval Type")
output_response = gr.Textbox(label="Response")

interface = gr.Interface(
    fn=process_query,
    inputs=[input_query, input_retrieval_type],
    outputs=output_response,
    title="RAG Question Answering System",
    description="Ask any question and get answers based on web search and documents.",
)

interface.launch()