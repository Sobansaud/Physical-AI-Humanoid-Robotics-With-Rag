"""
RAG (Retrieval-Augmented Generation) Engine with Qdrant
"""
import os
from typing import List, Dict, Any, Optional
import cohere
import asyncio
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "textbook_chunks"
EMBEDDING_DIM = 1024  # embed-english-v3.0


class RAGEngine:
    def __init__(self):
        if not COHERE_API_KEY:
            raise ValueError("COHERE_API_KEY is not set in the environment variables.")
        self.cohere = cohere.Client(api_key=COHERE_API_KEY)
        self.qdrant = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY if QDRANT_API_KEY else None
        )
        self._ensure_collection()
    
    def _ensure_collection(self):
        """Create collection if it doesn't exist"""
        try:
            collections = self.qdrant.get_collections().collections
            if not any(c.name == COLLECTION_NAME for c in collections):
                self.qdrant.create_collection(
                    collection_name=COLLECTION_NAME,
                    vectors_config=VectorParams(
                        size=EMBEDDING_DIM,
                        distance=Distance.COSINE
                    )
                )
        except Exception:
            pass  # Collection might already exist or Qdrant not available
    
    async def embed_query(self, text: str) -> List[float]:
        """Generate embedding for query text"""
        try:
            response = await asyncio.to_thread(self.cohere.embed, texts=[text], model="embed-english-v3.0", input_type="search_query")
            return response.embeddings[0]
        except Exception as e:
            raise RuntimeError(f"Error in embed_query: {e}")

    async def embed_document(self, text: str) -> List[float]:
        """Generate embedding for document text"""
        try:
            response = await asyncio.to_thread(self.cohere.embed, texts=[text], model="embed-english-v3.0", input_type="search_document")
            return response.embeddings[0]
        except Exception as e:
            raise RuntimeError(f"Error in embed_document: {e}")
    
    async def search_vectors(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search Qdrant for similar chunks"""
        try:
            query_vector = await self.embed_query(query)
            results = self.qdrant.search(
                collection_name=COLLECTION_NAME,
                query_vector=query_vector,
                limit=top_k
            )
            return [
                {
                    "text": hit.payload.get("text", "")[:500],  # Limit chunk size
                    "chapter": hit.payload.get("chapter", "Unknown"),
                    "score": hit.score
                }
                for hit in results
            ]
        except Exception:
            return []
    
    def build_prompt(self, question: str, context_chunks: List[Dict]) -> str:
        """Build concise prompt with retrieved context"""
        if context_chunks:
            context = "\n".join([
                f"[{c.get('chapter', '')}]: {c.get('text', '')}" 
                for c in context_chunks
            ])
            return f"""You are a robotics tutor. Answer concisely in 2-3 sentences.

Context:
{context}

Q: {question}
A:"""
        else:
            return f"""You are a robotics tutor. Answer concisely in 2-3 sentences about ROS2, Gazebo, Isaac Sim, or VLA.

Q: {question}
A:"""

    async def generate_answer(self, prompt: str) -> str:
        """Generate answer using Cohere command-r-08-2024"""
        try:
            response = await asyncio.to_thread(self.cohere.chat, message=prompt, model="command-r-08-2024", max_tokens=200, temperature=0.5)
            return response.text
        except AttributeError:
            # Fallback to generate method if chat is not available
            response = await asyncio.to_thread(self.cohere.generate, prompt=prompt, model="command-r-08-2024", max_tokens=200, temperature=0.5)
            return response.generations[0].text
        except Exception as e:
            raise RuntimeError(f"Error in generate_answer: {e}")
    
    async def ask(self, question: str) -> Dict[str, Any]:
        """Full RAG pipeline: embed → search → generate"""
        # Search for relevant chunks (reduced to 3)
        chunks = await self.search_vectors(question, top_k=3)
        
        # Build prompt with context
        prompt = self.build_prompt(question, chunks)
        
        # Generate answer
        answer = await self.generate_answer(prompt)
        
        # Build sources
        sources = [
            {"chapter": c["chapter"], "score": round(c["score"], 3)}
            for c in chunks if c.get("score", 0) > 0.7
        ]
        
        return {
            "answer": answer,
            "sources": sources
        }
    
    async def ask_selection(self, question: str, selection: str) -> Dict[str, Any]:
        """Answer question about selected text (no RAG)"""
        # Limit selection to 500 chars
        selection = selection[:500]
        prompt = f"""Explain this text concisely in 2-3 sentences:

Text: {selection}

Q: {question}
A:"""

        answer = await self.generate_answer(prompt)
        return {"answer": answer}
    
    async def index_chunk(self, chunk_id: str, text: str, chapter: str):
        """Index a single chunk into Qdrant"""
        embedding = await self.embed_document(text)
        self.qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=hash(chunk_id) % (2**63),
                    vector=embedding,
                    payload={"text": text, "chapter": chapter, "chunk_id": chunk_id}
                )
            ]
        )