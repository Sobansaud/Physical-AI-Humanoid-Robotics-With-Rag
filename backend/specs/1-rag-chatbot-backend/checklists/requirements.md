# Requirements Checklist

## Core Dependencies
- [x] `fastapi`: Web framework
- [x] `uvicorn`: ASGI Server
- [x] `openai`: Client for Gemini (via compatibility layer)
- [x] `qdrant-client`: Vector Database client
- [x] `python-dotenv`: Environment variable management
- [x] `pydantic`: Data validation

## External Services
- [x] **Google AI Studio**: Gemini 2.0 Flash API Access
- [x] **Qdrant Cloud**: Managed Vector Database

## Functional Requirements
- [x] **Latency**: Responses < 3 seconds (achieved with Gemini Flash).
- [x] **Accuracy**: Answers strictly grounded in retrieved context (System Prompt enforcement).
- [x] **Availability**: 24/7 Uptime via Dockerized container.
- [x] **Security**: API Keys managed via Environment Variables. No exposed secrets.