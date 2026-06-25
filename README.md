# SOC AI Copilot

An AI-powered cybersecurity assistant built with FastAPI, Streamlit, LangChain, Ollama, and ChromaDB.

The application provides:

- Retrieval-Augmented Generation (RAG)
- Category-aware document retrieval
- Section-aware retrieval
- Conversation memory
- Source attribution
- Web-based chat interface

## Demo

<img width="739" height="591" alt="image" src="https://github.com/user-attachments/assets/c7b0c3c1-7e6f-4d98-87a3-aef0f5f4ea12" />

## Installation

n3nu@LABORATORY:~/Demo$ python3 -m venv venv
n3nu@LABORATORY:~/Demo$ source venv/bin/activate
(venv) n3nu@LABORATORY:~/Demo$ git clone https://github.com/N3NU/soc-ai-copilot.git
(venv) n3nu@LABORATORY:~/Demo$ cd soc-ai-copilot/
(venv) n3nu@LABORATORY:~/Demo/soc-ai-copilot$ pip install -r requirements.txt
(venv) n3nu@LABORATORY:~/Demo/soc-ai-copilot$ python -m app.ingestion.ingest

## Modes

### CLI

(venv) n3nu@LABORATORY:~/Demo/soc-ai-copilot$ python -m app.main

### API

(venv) n3nu@LABORATORY:~/Demo/soc-ai-copilot$ uvicorn app.api:app --reload

### Web UI

(venv) n3nu@LABORATORY:~/Demo/soc-ai-copilot$ uvicorn app.api:app --reload
(venv) n3nu@LABORATORY:~/Demo/soc-ai-copilot$ streamlit run frontend.py

## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- Ollama
- ChromaDB
- Pydantic

## Roadmap

- [x] ChromaDB integration
- [x] Query rewriting
- [x] Category detection
- [x] Section detection
- [x] Session memory
- [x] FastAPI backend
- [x] Streamlit frontend
- [ ] Confidence scoring
- [ ] SQLite session storage
- [ ] Authentication
