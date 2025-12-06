"""
Tests for RAG endpoints
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock

# Import app
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health endpoint returns OK"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "physical-ai-textbook-api"


@pytest.mark.asyncio
async def test_ask_endpoint():
    """Test /api/ask returns answer"""
    mock_answer = {
        "answer": "ROS2 is a robotics middleware framework.",
        "sources": [{"chapter": "Module 1", "score": 0.85}]
    }
    
    with patch("app.main.RAGEngine") as MockRAG:
        mock_instance = MockRAG.return_value
        mock_instance.ask = AsyncMock(return_value=mock_answer)
        
        response = client.post(
            "/api/ask",
            json={"question": "What is ROS2?"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "sources" in data


@pytest.mark.asyncio
async def test_ask_selection_endpoint():
    """Test /api/ask-selection uses selection as context"""
    mock_answer = {"answer": "This text explains node communication."}
    
    with patch("app.main.RAGEngine") as MockRAG:
        mock_instance = MockRAG.return_value
        mock_instance.ask_selection = AsyncMock(return_value=mock_answer)
        
        response = client.post(
            "/api/ask-selection",
            json={
                "question": "Explain this",
                "selection": "ROS2 nodes communicate via topics"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data


def test_ask_invalid_request():
    """Test /api/ask rejects invalid requests"""
    response = client.post("/api/ask", json={})
    assert response.status_code == 422  # Validation error


def test_ask_selection_invalid_request():
    """Test /api/ask-selection rejects invalid requests"""
    response = client.post(
        "/api/ask-selection",
        json={"question": "test"}  # Missing selection
    )
    assert response.status_code == 422
