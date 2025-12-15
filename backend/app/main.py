"""
FastAPI backend for Physical AI Textbook RAG Chatbot
"""
from dotenv import load_dotenv
load_dotenv()  # Load .env file before anything else

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from .rag import RAGEngine


app = FastAPI(
    title="Physical AI Textbook API",
    description="RAG-powered Q&A for robotics education (Cohere)",
    version="2.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*", 
        "http://localhost:3000",
        "https://physical-ai-humanoid-robotics-with.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class AskRequest(BaseModel):
    question: str


class AskSelectionRequest(BaseModel):
    question: str
    selection: str


class AskResponse(BaseModel):
    answer: str
    sources: List[dict] = []


# Health Check
@app.get("/")
async def root():
    return {"message": "Physical AI Textbook API (Cohere)", "docs": "/docs", "health": "/api/health"}


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "physical-ai-textbook-api", "model": "command-r-08-2024"}


# RAG Endpoints
@app.post("/api/ask", response_model=AskResponse)
async def ask_question(request: AskRequest):
    """RAG Q&A on full textbook content"""
    try:
        rag = RAGEngine()
        result = await rag.ask(request.question)
        return AskResponse(
            answer=result["answer"],
            sources=result.get("sources", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ask-selection", response_model=AskResponse)
async def ask_about_selection(request: AskSelectionRequest):
    """Q&A about selected text"""
    try:
        rag = RAGEngine()
        result = await rag.ask_selection(
            question=request.question,
            selection=request.selection
        )
        return AskResponse(answer=result["answer"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
