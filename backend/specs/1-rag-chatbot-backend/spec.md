# Backend Specification: Physical AI RAG System

## 1. System Overview
The backend serves as the intelligence layer for the Physical AI Textbook. It intercepts user queries, retrieves context from vector storage, and synthesizes answers using Google's Gemini models.

## 2. Architecture

### 2.1 Tech Stack
-   **Runtime**: Python 3.11+
-   **Web Server**: FastAPI + Uvicorn
-   **LLM**: Google Gemini 2.0 Flash (via `openai` SDK)
-   **Embeddings**: Google `text-embedding-004` (768d)
-   **Vector DB**: Qdrant Cloud

### 2.2 Data Flow
1.  **Request**: Frontend sends JSON payload to `POST /api/ask`.
2.  **Embedding**: Backend embeds query using `text-embedding-004`.
3.  **Retrieval**: Qdrant searches `physical_ai_textbook` collection for top-k similar chunks.
4.  **Synthesis**: Gemini 2.0 Flash receives `(System Prompt + Context + Question)`.
5.  **Response**: JSON containing the answer is sent back.

## 3. API Reference

### 3.1 `POST /api/ask`
**Summary**: Main RAG question answering endpoint.

**Request Body**:
```json
{
  "question": "string"
}
```

**Response**:
```json
{
  "answer": "string",
  "sources": ["string"]
}
```

### 3.2 `POST /api/ask-selection`
**Summary**: Contextual explanation of selected text.

**Request Body**:
```json
{
  "selection": "string",
  "question": "string (optional)"
}
```

**Response**:
```json
{
  "answer": "string"
}
```

### 3.3 `GET /api/health`
**Summary**: Service health check.
**Response**: `{"status": "ok", "model": "gemini-2.0-flash"}`

## 4. Configuration
Required Environment Variables:
-   `GEMINI_API_KEY`: API Key for Google AI Studio.
-   `QDRANT_URL`: URL of Qdrant instance.
-   `QDRANT_API_KEY`: API Key for Qdrant.
