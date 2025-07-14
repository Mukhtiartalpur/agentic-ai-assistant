# rag.py

import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Define path to your PDF folder
PDF_DIR = "./data"
VECTORSTORE_DIR = "./vectorstore"

def load_and_split_pdfs(pdf_dir):
    loader = PyPDFDirectoryLoader(pdf_dir)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(documents)

def create_vectorstore(chunks):
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embedding)
    vectorstore.save_local(VECTORSTORE_DIR)
    return vectorstore

if __name__ == "__main__":
    print("Loading and splitting PDFs...")
    chunks = load_and_split_pdfs(PDF_DIR)

    print("Creating vectorstore...")
    create_vectorstore(chunks)
    
    print("✅ Vectorstore created and saved at:", VECTORSTORE_DIR)
