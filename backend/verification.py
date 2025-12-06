import sys
import os
import asyncio
from dotenv import load_dotenv

# Load .env BEFORE imports that rely on env vars
load_dotenv()

from app.rag import RAGEngine

async def verify():
    print("----------------------------------------------------------------")
    print("Starting Setup Verification")
    print("----------------------------------------------------------------")
    
    # Check Environment Variables
    gemini_key = os.getenv("GEMINI_API_KEY")
    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_key = os.getenv("QDRANT_API_KEY")
    
    print(f"GEMINI_API_KEY Present: {bool(gemini_key)}")
    print(f"QDRANT_URL: {qdrant_url}")
    print(f"QDRANT_API_KEY Present: {bool(qdrant_key)}")
    
    if not gemini_key:
        print("❌ CRITICAL: GEMINI_API_KEY is missing!")
        return

    print("\n[Init] Initializing RAGEngine...")
    try:
        rag = RAGEngine()
        print("✅ RAGEngine initialized.")
    except Exception as e:
        print(f"❌ Failed to initialize RAGEngine: {e}")
        import traceback
        traceback.print_exc()
        return

    print("\n[Test] Running Embedding Test (text-embedding-004)...")
    try:
        embedding = await rag.embed_query("test query")
        print(f"✅ Embedding successful. Vector length: {len(embedding)}")
    except Exception as e:
        print(f"❌ Embedding failed: {e}")
        # Continue to see if chat works even if embedding fails (unlikely for RAG but good to know)
    
    print("\n[Test] Running Chat Test (gemini-2.0-flash)...")
    try:
        # Direct test of generate_answer to isolate LLM
        response = await rag.generate_answer("Hello, are you working?")
        print(f"✅ Chat response received:\n{response}")
    except Exception as e:
        print(f"❌ Chat generation failed: {e}")

    print("\n----------------------------------------------------------------")
    print("Verification Complete")
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    asyncio.run(verify())
