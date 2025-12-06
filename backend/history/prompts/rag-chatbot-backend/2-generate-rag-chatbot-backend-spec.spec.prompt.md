---
title: Physical AI Chatbot Backend
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# Prompt: Generate RAG Chatbot Backend Specification

## Context
We are creating the backend for the "Physical AI Textbook". This will be a RAG (Retrieval Augmented Generation) system that answers student questions based on the textbook content.

## Objective
Generate a comprehensive technical specification (`spec.md`) for the backend.

## Requirements
1.  **Core Technology**:
    -   **Server**: FastAPI (Python).
    -   **LLM**: Google Gemini 2.0 Flash (`gemini-2.0-flash`).
    -   **Embeddings**: Google `text-embedding-004`.
    -   **Vector DB**: Qdrant (Cloud).
    -   **Deployment**: Docker (Hugging Face Spaces compatible).

2.  **API Endpoints**:
    -   `POST /api/ask`: Primary RAG endpoint. Accepts `question`, returns `answer` and `sources`.
    -   `POST /api/ask-selection`: Explains specific text selected by the user.
    -   `GET /api/health`: Status check returning current model info.

3.  **Architecture Rules**:
    -   Use `openai` Python SDK with `base_url` set to Google's compatibility endpoint.
    -   Stateless architecture (no user sessions, no SQL DB required for MVP).
    -   Environment variables for all keys (`GEMINI_API_KEY`, `QDRANT_URL`).

4.  **Deliverables in Spec**:
    -   System Overview.
    -   API Reference (Requests/Responses).
    -   Data Flow Diagram description.
    -   Configuration details.

Please write the full `spec.md`.