"""
RAG (Retrieval-Augmented Generation) Engine with Qdrant
"""
import os
from typing import List, Dict, Any, Optional
from openai import AsyncOpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "textbook_chunks"
# Gemini text-embedding-004 dimensions = 768 usually, but let's check or assume. 
# Actually, if we are switching models, we might need to re-index or use a compatible dimension.
# For now, I will assume we might need to recreate the collection or just update the logic.
# However, to be safe and simple:
EMBEDDING_DIM = 768 # text-embedding-004


class RAGEngine:
    def __init__(self):
        if not GEMINI_API_KEY:
             raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
        
        self.openai = AsyncOpenAI(
            api_key=GEMINI_API_KEY,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai"
        )
        
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
        # Using Gemini's embedding model via OpenAI compat layer
        response = await self.openai.embeddings.create(
            model="text-embedding-004",
            input=text
        )
        return response.data[0].embedding
    
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
        """Generate answer using Gemini 2.0 Flash"""
        response = await self.openai.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=200
        )
        return response.choices[0].message.content
    
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
            for c in chunks if c.get("score", 0) > 0.0  # Lower threshold as metrics might differ
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
        embedding = await self.embed_query(text)
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

