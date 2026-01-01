import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import RetrievalQA

# ---------------------------------------------------------
# PART 1: INGESTION (Read PDF -> Vector DB)
# ---------------------------------------------------------
async def process_pdf(file_path: str):
    """
    Reads a PDF, splits it into chunks, and creates a FAISS vector store.
    """
    try:
        # 1. Load PDF
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        # 2. Split Text
        # 1000 characters per chunk with 200 overlap is a standard "Goldilocks" zone
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        
        # 3. Create Embeddings & Vector Store
        # Using the free Hugging Face model (runs locally on CPU)
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # Create the database in RAM
        vector_store = FAISS.from_documents(chunks, embeddings)
        
        return vector_store, len(chunks)

    except Exception as e:
        # Pass the error up to the route handler
        raise e