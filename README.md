# 📄 Chat with Your PDF (Backend)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green) ![LangChain](https://img.shields.io/badge/LangChain-0.0.1%2B-orange) ![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)

A powerful **Retrieval-Augmented Generation (RAG)** backend that allows users to upload PDF documents and ask questions about their content in natural language. This API handles document ingestion, embedding generation, vector storage, and LLM-based query processing using **free, open-source models**.

## 🚀 Features

* **PDF Ingestion:** Upload and process PDF documents instantly.
* **Smart Chunking:** Splits large documents into manageable context windows using `RecursiveCharacterTextSplitter`.
* **Vector Search:** Uses **FAISS (Facebook AI Similarity Search)** for high-speed local similarity search.
* **Open-Source LLM:** Uses **Mistral-7B** (via Hugging Face Hub) to generate accurate answers without OpenAI costs.
* **RESTful API:** Built with **FastAPI** for easy integration with any frontend (React, Vue, Streamlit, etc.).
* **Robust Validation:** Uses Pydantic for strict data contracts and automatic documentation.

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Orchestration:** LangChain
* **LLM Provider:** Hugging Face Hub (Mistral-7B-Instruct)
* **Embeddings:** HuggingFace Embeddings (`all-MiniLM-L6-v2`)
* **Vector Store:** FAISS (CPU)
* **PDF Parsing:** PyPDF

## 📂 Folder Structure

```bash
chat-with-pdf-backend/
├── main.py              # The core application logic and API endpoints
├── requirements.txt     # List of dependencies
├── .env                 # Environment variables (API Keys)
└── README.md            # Project documentation