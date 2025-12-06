# Backend Specification: Physical AI RAG Chatbot

## Overview
A lightweight, high-performance RAG backend using FastAPI and Google Gemini 2.0 Flash. It serves the Physical AI Textbook frontend.

## Architecture
-   **API Layer**: FastAPI (`app/main.py`)
-   **Logic Layer**: RAGEngine (`app/rag.py`)
-   **Database**: Qdrant (Vector Store for textbook chunks)
-   **AI Engine**: Google Gemini 2.0 Flash (Chat) & text-embedding-004 (Embeddings)

## API Endpoints

### `POST /api/ask`
-   **Input**: `{ "question": "What is ROS2?" }`
-   **Output**: `{ "answer": "...", "sources": [...] }`
-   **Logic**: Embeds question -> Searches Qdrant -> Prompts Gemini with Context -> Returns Answer.

### `POST /api/ask-selection`
-   **Input**: `{ "question": "Explain this", "selection": "selected text..." }`
-   **Output**: `{ "answer": "..." }`
-   **Logic**: Prompts Gemini directly with the selection and question.

### `GET /api/health`
-   **Output**: `{ "status": "ok", "model": "gemini-2.0-flash" }`

## Configuration
-   `GEMINI_API_KEY`: Required.
-   `QDRANT_URL/API_KEY`: Required for connection.
