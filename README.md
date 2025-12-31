📄 Chat with Your PDF (Backend)
A powerful Retrieval-Augmented Generation (RAG) backend that allows users to upload PDF documents and ask questions about their content in natural language. This API handles document ingestion, embedding generation, vector storage, and LLM-based query processing.

🚀 Features
PDF Ingestion: Upload and process PDF documents instantly.

Smart Chunking: Splits large documents into manageable context windows using RecursiveCharacterTextSplitter.

Vector Search: Uses FAISS (Facebook AI Similarity Search) for high-speed local similarity search.

Context-Aware Answers: Retrieves only the relevant sections of the PDF to generate accurate answers using OpenAI's GPT models.

RESTful API: Built with FastAPI for easy integration with any frontend (React, Vue, Streamlit, etc.).

🛠️ Tech Stack
Framework: FastAPI

Orchestration: LangChain

LLM Provider: OpenAI (GPT-3.5/GPT-4)

Vector Store: FAISS (CPU)

PDF Parsing: PyPDF
