# 📄 Chat with Your PDF (Backend)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green) ![LangChain](https://img.shields.io/badge/LangChain-0.0.1%2B-orange)

A powerful **Retrieval-Augmented Generation (RAG)** backend that allows users to upload PDF documents and ask questions about their content in natural language. This API handles document ingestion, embedding generation, vector storage, and LLM-based query processing.

## 🚀 Features

* **PDF Ingestion:** Upload and process PDF documents instantly.
* **Smart Chunking:** Splits large documents into manageable context windows using `RecursiveCharacterTextSplitter`.
* **Vector Search:** Uses **FAISS (Facebook AI Similarity Search)** for high-speed local similarity search.
* **Context-Aware Answers:** Retrieves only the relevant sections of the PDF to generate accurate answers using OpenAI's GPT models.
* **RESTful API:** Built with **FastAPI** for easy integration with any frontend (React, Vue, Streamlit, etc.).

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Orchestration:** LangChain
* **LLM Provider:** OpenAI (GPT-3.5/GPT-4)
* **Vector Store:** FAISS (CPU)
* **PDF Parsing:** PyPDF

## 📂 Folder Structure

```bash
chat-with-pdf-backend/
├── main.py              # The core application logic and API endpoints
├── requirements.txt     # List of dependencies
├── .env                 # Environment variables (API Keys)
└── README.md            # Project documentation
