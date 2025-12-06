#!/usr/bin/env python3
"""
Index MDX content into Qdrant for RAG search
"""
import os
import re
import asyncio
from pathlib import Path
from typing import List, Dict

# Add parent to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.rag import RAGEngine

DOCS_PATH = Path(__file__).parent.parent.parent / "docs"
CHUNK_SIZE = 1000  # characters per chunk
CHUNK_OVERLAP = 200


def extract_text_from_mdx(content: str) -> str:
    """Extract plain text from MDX, preserving code blocks"""
    # Remove frontmatter
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    
    # Keep code blocks but mark them
    content = re.sub(r'```(\w+)?\n(.*?)```', r'[CODE]\2[/CODE]', content, flags=re.DOTALL)
    
    # Remove mermaid diagrams (keep for context but mark)
    content = re.sub(r'```mermaid\n(.*?)```', r'[DIAGRAM]', content, flags=re.DOTALL)
    
    # Remove HTML/JSX tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Remove markdown links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove images
    content = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', content)
    
    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()


def chunk_text(text: str, chapter: str) -> List[Dict]:
    """Split text into chunks with overlap"""
    chunks = []
    
    # Split by paragraphs first
    paragraphs = text.split('\n\n')
    
    current_chunk = ""
    chunk_index = 0
    
    for para in paragraphs:
        if len(current_chunk) + len(para) < CHUNK_SIZE:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append({
                    "chunk_id": f"{chapter}_{chunk_index}",
                    "text": current_chunk.strip(),
                    "chapter": chapter
                })
                chunk_index += 1
                
                # Overlap: keep last portion
                words = current_chunk.split()
                overlap_words = words[-CHUNK_OVERLAP//5:] if len(words) > CHUNK_OVERLAP//5 else []
                current_chunk = " ".join(overlap_words) + "\n\n" + para + "\n\n"
            else:
                current_chunk = para + "\n\n"
    
    # Don't forget last chunk
    if current_chunk.strip():
        chunks.append({
            "chunk_id": f"{chapter}_{chunk_index}",
            "text": current_chunk.strip(),
            "chapter": chapter
        })
    
    return chunks


def get_chapter_name(file_path: Path) -> str:
    """Extract chapter name from file path"""
    # Get relative path from docs folder
    rel_path = file_path.relative_to(DOCS_PATH)
    
    # Convert to readable chapter name
    parts = list(rel_path.parts)
    
    # Remove file extension
    if parts:
        parts[-1] = parts[-1].replace('.mdx', '').replace('.md', '')
    
    return " / ".join(parts)


async def index_all_content():
    """Index all MDX files"""
    rag = RAGEngine()
    
    # Find all MDX files
    mdx_files = list(DOCS_PATH.glob("**/*.mdx")) + list(DOCS_PATH.glob("**/*.md"))
    
    print(f"Found {len(mdx_files)} MDX files to index")
    
    total_chunks = 0
    
    for file_path in mdx_files:
        chapter = get_chapter_name(file_path)
        print(f"Processing: {chapter}")
        
        # Read content
        content = file_path.read_text(encoding='utf-8')
        
        # Extract text
        text = extract_text_from_mdx(content)
        
        # Chunk
        chunks = chunk_text(text, chapter)
        
        print(f"  → {len(chunks)} chunks")
        
        # Index each chunk
        for chunk in chunks:
            await rag.index_chunk(
                chunk_id=chunk["chunk_id"],
                text=chunk["text"],
                chapter=chunk["chapter"]
            )
        
        total_chunks += len(chunks)
    
    print(f"\n✅ Indexed {total_chunks} chunks from {len(mdx_files)} files")


if __name__ == "__main__":
    asyncio.run(index_all_content())
