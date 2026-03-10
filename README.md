### AI RAG Chatbot (Document Question Answering)

An AI-powered Retrieval Augmented Generation (RAG) chatbot that answers questions from custom documents using vector search and large language models.

The system extracts text from documents, converts them into embeddings, stores them in a vector database, retrieves relevant information for user queries, and generates answers using an LLM.

## Project Overview

This project implements a full **RAG (Retrieval Augmented Generation)** pipeline:

User Query  
↓  
Vector Similarity Search  
↓  
Relevant Document Retrieval  
↓  
Context Injection  
↓  
LLM Answer Generation  

The chatbot ensures answers are generated **only from the provided documents**, reducing hallucinations.


## Features

- Document ingestion (PDF, TXT, Markdown)
- Text chunking with overlap
- Embedding generation using Sentence Transformers
- Vector similarity search using FAISS
- Context-aware question answering
- Dynamic knowledge addition
- Conversation memory
- Streamlit web interface
- Groq LLM API integration for fast inference

## Tech Stack

Frontend  
- Streamlit

Backend  
- FastAPI

Vector Database  
- FAISS

Embeddings  
- Sentence Transformers (all-MiniLM-L6-v2)

LLM Inference  
- Groq API (Llama3 models)

Language  
- Python

Libraries  
- numpy  
- pandas  
- requests  
- pypdf  

## Architecture

Document Loader  
↓  
Text Chunking  
↓  
Embedding Generation  
↓  
FAISS Vector Index  
↓  
Query Retrieval  
↓  
Context Construction  
↓  
LLM Generation  
↓  
Answer Display
# Live demo link: https://aichatbot-nasts4idxez6vduls2dq9z.streamlit.app
