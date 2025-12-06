---
title: Physical AI Chatbot Backend
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# Physical AI Textbook RAG Backend

This is the RAG (Retrieval Augmented Generation) backend for the Physical AI Textbook. It uses **Google Gemini 2.0 Flash** for reasoning and **Qdrant** for vector retrieval, served via **FastAPI**.

## Features

-   **Gemini 2.0 Flash**: State-of-the-art reasoning via Google's `generativelanguage` API (using the OpenAI SDK compatibility layer).
-   **RAG Engine**: Retrieves context from Qdrant (`text-embedding-004` embeddings) to answer student questions.
-   **Contextual Explanations**: Dedicated endpoint for explaining selected text from the frontend.
-   **Zero Bloat**: No authentication, user management, or legacy features. Purely a knowledge serving API.

## API Endpoints

### 1. `POST /api/ask`
*Main RAG Endpoint.*
-   **Body**: `{ "question": "What is inverse kinematics?" }`
-   **Response**: `{ "answer": "...", "sources": [...] }`

### 2. `POST /api/ask-selection`
*Explain Selected Text.*
-   **Body**: `{ "selection": "Selected text...", "question": "Explain this" }`
-   **Response**: `{ "answer": "..." }`

### 3. `GET /api/health`
*Health Check.*
-   **Response**: `{ "status": "ok", "model": "gemini-2.0-flash" }`

## Setup & Run

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

### Environment Variables
Create a `.env` file:
```ini
GEMINI_API_KEY=your_key_here
QDRANT_URL=your_url_here
QDRANT_API_KEY=your_key_here
```

## Deployment

Designed for **Hugging Face Spaces** (Docker SDK).
-   **Port**: 7860
-   **Authentication**: None (Public API)
