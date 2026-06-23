from fastapi import FastAPI
from pydantic import BaseModel

from app.services.copilot_service import process_query
from app.services.session_store import sessions
from app.config import MAX_CHAT_HISTORY

app = FastAPI()


class QueryRequest(BaseModel):
    session_id: str
    query: str


class QueryResponse(BaseModel):
    query: str
    rewritten_query: str
    category: str | None
    section: str | None
    current_topic: str | None
    source: str
    answer: str
    distance: float


@app.get("/")
def root():
    return {
        "message": "SOC AI Copilot API"
    }


@app.post("/analyze", response_model=QueryResponse)
def analyze(request: QueryRequest):

    if request.session_id not in sessions:
        sessions[request.session_id] = {
        "chat_history": [],
        "current_topic": None
    }

    session = sessions[request.session_id]

    result = process_query(
    query=request.query,
    chat_history=session["chat_history"],
    current_topic=session["current_topic"]
    )

    session["current_topic"] = result["current_topic"]

    session["chat_history"].append(
        f"User: {result['rewritten_query']}"
    )

    session["chat_history"].append(
        f"Assistant: {result['response']}"
    )

    session["chat_history"] = session["chat_history"][-MAX_CHAT_HISTORY:]

    return QueryResponse(
        query=request.query,
        rewritten_query=result["rewritten_query"],
        category=result["category"],
        section=result["section"],
        current_topic=result["current_topic"],
        source=result["source"],
        answer=result["response"],
        distance=result["distance"]
    )

