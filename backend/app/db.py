"""
Database connection and helpers for SQLite (aiosqlite)
Migrated from PostgreSQL/Neon due to auth issues.
"""
import os
import sys
import json
import aiosqlite
import tempfile
from typing import Optional, List, Dict, Any
from pathlib import Path

# Database file path - cross-platform support
# On Windows: uses temp directory
# On Linux/Render: uses /tmp
def get_db_path():
    env_path = os.getenv("DATABASE_PATH")
    if env_path:
        return env_path
    
    # Use temp directory for cross-platform compatibility
    if sys.platform == "win32":
        # Windows: use local data folder
        data_dir = Path(__file__).parent.parent / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        return str(data_dir / "textbook.db")
    else:
        # Linux/Render: use /tmp
        return "/tmp/textbook.db"

DB_PATH = get_db_path()

# Ensure directory exists for the database file
db_dir = Path(DB_PATH).parent
if db_dir and not db_dir.exists():
    db_dir.mkdir(parents=True, exist_ok=True)

# Shared connection for the app
_db_connection: Optional[aiosqlite.Connection] = None


async def get_connection() -> aiosqlite.Connection:
    """Get shared database connection"""
    global _db_connection
    if _db_connection is None:
        _db_connection = await aiosqlite.connect(DB_PATH)
        _db_connection.row_factory = aiosqlite.Row
    return _db_connection


async def close_pool():
    """Close the database connection"""
    global _db_connection
    if _db_connection:
        await _db_connection.close()
        _db_connection = None


async def execute(query: str, *args) -> str:
    """Execute a query (converts $1, $2 to ? placeholders)"""
    sqlite_query = _convert_params(query)
    conn = await get_connection()
    await conn.execute(sqlite_query, args)
    await conn.commit()
    return "OK"


async def fetch_one(query: str, *args) -> Optional[Dict[str, Any]]:
    """Fetch single row"""
    sqlite_query = _convert_params(query)
    conn = await get_connection()
    async with conn.execute(sqlite_query, args) as cursor:
        row = await cursor.fetchone()
        return dict(row) if row else None


async def fetch_all(query: str, *args) -> List[Dict[str, Any]]:
    """Fetch all rows"""
    sqlite_query = _convert_params(query)
    conn = await get_connection()
    async with conn.execute(sqlite_query, args) as cursor:
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]


def _convert_params(query: str) -> str:
    """Convert PostgreSQL $1, $2 params to SQLite ? params"""
    import re
    return re.sub(r'\$\d+', '?', query)


# SQL Schema for SQLite
SCHEMA = """
-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT,
    github_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User levels (from quiz)
CREATE TABLE IF NOT EXISTS user_levels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    level TEXT DEFAULT 'beginner',
    quiz_score INTEGER,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat history
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    sources TEXT DEFAULT '[]',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Quiz responses
CREATE TABLE IF NOT EXISTS quiz_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    question_id INTEGER NOT NULL,
    answer TEXT NOT NULL,
    is_correct INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Urdu translation cache
CREATE TABLE IF NOT EXISTS urdu_cache (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_slug TEXT UNIQUE NOT NULL,
    urdu_content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Personalized content cache
CREATE TABLE IF NOT EXISTS personalized_cache (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_slug TEXT NOT NULL,
    user_level TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(chapter_slug, user_level)
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_chat_history_user ON chat_history(user_id);
CREATE INDEX IF NOT EXISTS idx_quiz_responses_user ON quiz_responses(user_id);
CREATE INDEX IF NOT EXISTS idx_urdu_cache_slug ON urdu_cache(chapter_slug);
"""


async def init_db():
    """Initialize database schema"""
    conn = await get_connection()
    await conn.executescript(SCHEMA)
    await conn.commit()
    print(f"✅ Database initialized at {DB_PATH}")
