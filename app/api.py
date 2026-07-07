from fastapi import FastAPI
from pydantic import BaseModel

from app.services.copilot_service import process_query
from app.database.schema import initialize_database
from app.database.session_repository import create_session, get_chat_history, get_current_topic, update_current_topic, save_message

app = FastAPI()

initialize_database()

class QueryRequest(BaseModel):
    session_id: str
    query: str


class QueryResponse(BaseModel):
    query: str
    rewritten_query: str
    category: str | None
    section: str | None
    current_topic: str | None
    source: str | None
    answer: str
    distance: float | None
    confidence: str | None


@app.get("/")
def root():
    return {
        "message": "SOC AI Copilot API"
    }


@app.post("/analyze", response_model=QueryResponse)
def analyze(request: QueryRequest):

    create_session(request.session_id)

    history = get_chat_history(request.session_id)

    current_topic = get_current_topic(request.session_id)

    result = process_query(
    query=request.query,
    chat_history=history,
    current_topic=current_topic
    )

    update_current_topic(
        request.session_id,
        result["current_topic"]
    )

    save_message(request.session_id, "user", result["rewritten_query"])

    save_message(request.session_id, "assistant", result["response"])

    return QueryResponse(
        query=request.query,
        rewritten_query=result["rewritten_query"],
        category=result["category"],
        section=result["section"],
        current_topic=result["current_topic"],
        source=result["source"],
        answer=result["response"],
        distance=result["distance"],
        confidence=result["confidence"]
    )

