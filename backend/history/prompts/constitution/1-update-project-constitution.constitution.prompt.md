---
id: 1
title: Update Project Constitution
stage: constitution
date: 2025-12-06
surface: agent
model: claude-opus-4-5-20251101
feature: none
branch: 1-ai-textbook-frontend
user: user
command: /sp.constitution
labels: ["constitution", "update"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
---

## Prompt

```text
Project: Interactive RAG-Powered Book (OpenAI Agents + SpecifyKit + Claude CLI)

Core Principles:
- Source-bound accuracy (answers must be grounded strictly in book text or user-selected text)
- Transparency of reasoning (RAG citations must be clear and traceable)
- Reliability (no hallucinations; no invented information)
- User-centric clarity (answers must be clear for general readers, not technical experts)
- Safety-first (no harmful, political, or biased interpretations beyond the text)
- Deterministic behavior (same input → consistent answer)

Key Standards:
1. Retrieval Discipline:
   - If user highlights text: ONLY answer from highlighted text.
   - If user asks general question: answer from full book corpus embedded in Qdrant.
   - If no relevant text retrieved: say “No supporting information found in the book.”

2. RAG Response Structure:
   - Short summary answer (max 4 lines)
   - Supporting evidence (quoted from book)
   - Citation ID (Qdrant vector reference key)

3. Allowed Knowledge:
   - Only content present in the book.
   - No external facts, no guessing, no assumptions.

4. Data Governance:
   - All chunks must map to Neon Postgres metadata rows.
   - Every AI output must reference correct chunk_id(s).

5. Writing Style Guidelines:
   - Grade level: Flesch-Kincaid 8–10 (simple, clear)
   - Tone: Neutral, educational, supportive
   - Format: short paragraphs, bullet points when possible

Constraints:
- Chatbot must refuse to answer anything outside the book scope.
- Maximum answer length: 200 tokens unless user explicitly requests a longer explanation.
- No hallucinated citations; if retrieval fails, respond safely.
- All internal reasoning must follow SpecifyKit Task → Agent → Contract structure.

Operational Rules:
- Always perform RAG first before answering.
- If user selects text, bypass full retrieval and use ONLY that text.
- If selected text is < 10 characters, fallback to normal RAG.

Success Criteria:
- 100% answers grounded in book’s actual text
- Zero hallucinations in testing
- Latency under 1.5 seconds per query (FastAPI + Qdrant hybrid search)
- All answers include book-based citations
- Smooth integration with SpecifyKit + Claude CLI workflows

Output Quality Benchmarks:
- Accuracy: Must match source text exactly
- Relevance: Only content that answers the user’s question
- Clarity: Understandable by non-technical readers
- Consistency: Identical input → identical answer every time
```

## Response snapshot

The project constitution (.specify/memory/constitution.md) has been updated to version `0.1.0`. This minor version bump reflects the addition of new core principles, key standards, constraints, operational rules, success criteria, and output quality benchmarks derived from the user's input. No files require manual follow-up.

Suggested commit message: `docs: amend constitution to v0.1.0 (initial principles, standards, and rules)`

## Outcome

- ✅ Impact: Constitution updated with new project principles.
- 🧪 Tests: N/A
- 📁 Files: .specify/memory/constitution.md updated.
- 🔁 Next prompts: Continue with project development based on the updated constitution.
- 🧠 Reflection: Successfully updated the project constitution based on user input, ensuring consistency with related templates.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
