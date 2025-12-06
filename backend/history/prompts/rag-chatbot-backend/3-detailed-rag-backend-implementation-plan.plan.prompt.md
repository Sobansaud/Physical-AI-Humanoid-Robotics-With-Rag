---
title: Physical AI Chatbot Backend
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# Prompt: Create Implementation Plan

## Context
We have a specification for a FastAPI-based RAG backend using Gemini 2.0 Flash and Qdrant.

## Objective
Create a detailed, phase-by-phased implementation plan (`plan.md`) to build this system.

## Plan Structure

### Phase 1: Foundation
-   Project scaffolding (`app/`).
-   Dependency installation (`fastapi`, `openai`, `qdrant-client`).
-   Environment setup (`.env`).

### Phase 2: Core Logic (`rag.py`)
-   Implement `RAGEngine` class.
-   Setup `AsyncOpenAI` client for Gemini.
-   Implement embedding generation with `text-embedding-004`.
-   Implement retrieval and answer generation.

### Phase 3: API Layer (`main.py`)
-   Setup FastAPI app with CORS (allow frontend URL).
-   Implement `/api/ask` and `/api/ask-selection` endpoints.
-   Integrate `RAGEngine`.

### Phase 4: Deployment
-   Create `Dockerfile`.
-   Deployment instructions for Hugging Face Spaces.

Please generate the `plan.md` file following this structure.