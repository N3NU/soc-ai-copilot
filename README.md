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

### Prerequisites (Model can be changed in soc-ai-copilot/config.py)

Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Start Ollama:
```bash
ollama serve
```
Pull the models:
```bash
ollama pull llama3
```
```bash
ollama pull qwen2.5:0.5b
```

### Set up environment and clone SOC AI Copilot
Use following two commands to create a virtual environment, optional but highly recommended (do it)
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
Clone SOC AI Copilot
```bash
git clone https://github.com/N3NU/soc-ai-copilot.git
```
```bash
cd soc-ai-copilot
```
```bash
pip install -r requirements.txt
```
```bash
python -m app.ingestion.ingest
```

## Modes

### CLI
```bash
python -m app.main
```
### API
```bash
uvicorn app.api:app --reload
```
### Web UI
```bash
uvicorn app.api:app --reload
```
```bash
streamlit run frontend.py
```

## Example Queries

- What are ransomware indicators?
- How do I contain a phishing incident?
- What are psexec indicators?
- Explain impossible travel alerts.

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
- [x] Confidence scoring
- [x] SQLite session storage
- [ ] Authentication
