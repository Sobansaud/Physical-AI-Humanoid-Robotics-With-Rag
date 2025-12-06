# Prompt 01: Physical AI RAG Backend Generation

## Role
You are an expert Backend Engineer and AI Architect.

## Objective
Create a lightweight, high-performance RAG (Retrieval Augmented Generation) backend for the "Physical AI Textbook" project.

## Tech Stack
-   **Framework**: FastAPI (Python).
-   **AI Model**: Google Gemini 2.0 Flash (`gemini-2.0-flash`).
-   **Integration**: Use the `openai` Python SDK (via Google's compatibility base URL).
-   **Embeddings**: `text-embedding-004` (768 dimensions).
-   **Vector Database**: Qdrant (Cloud/Local).
-   **Deployment**: Docker (Hugging Face Spaces compatible).

## Functional Requirements
1.  **RAG QA Endpoint** (`/api/ask`):
    -   Accept a user question.
    -   Retrieve relevant context from Qdrant.
    -   Generate an answer using Gemini 2.0 Flash.
    -   Return answer and source chunks.

2.  **Selection Explanation** (`/api/ask-selection`):
    -   Accept selected text from the frontend.
    -   Provide a contextual explanation or definition of the selection.

3.  **No Authentication**:
    -   The API is public-read for the textbook. Remove all user management, login, or complex state.

4.  **Simplicity**:
    -   Clean code structure: `app/main.py`, `app/rag.py`.
    -   Environment variable configuration (`.env`).

## Output
Please generate the complete codebase including `requirements.txt`, `Dockerfile`, and the FastAPI application logic.
