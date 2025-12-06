# Implementation Tasks

## Setup & Config
- [x] Initialize Git repository
- [x] Create virtual environment
- [x] Create `.env` file
- [x] Install dependencies (`fastapi`, `openai`, `qdrant-client`)

## Core Modules
- [x] Implement `RAGEngine` class in `app/rag.py`
- [x] Configure Gemini API client
- [x] Configure Qdrant client
- [x] Implement embedding generation (`embed_query`)
- [x] Implement answer generation (`generate_answer`)

## API Layer
- [x] Create FastAPI app structure (`app/main.py`)
- [x] Configure CORS (`localhost:3000`, production URL)
- [x] Implement `POST /api/ask`
- [x] Implement `POST /api/ask-selection`
- [x] Implement `GET /api/health`

## Optimization & Cleanup
- [x] Remove legacy authentication code
- [x] Remove unused SQLite database code
- [x] Update `requirements.txt` to minimal set
- [x] Optimize prompt templates for Gemini

## Deployment
- [x] Create `Dockerfile`
- [x] Verify local build
- [x] Prepare for Hugging Face Spaces deployment
