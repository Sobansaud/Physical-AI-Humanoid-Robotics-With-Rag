<!--
Version change: None (initial creation) → 0.1.0
Modified principles:
- Original template principles replaced with user-defined principles:
    - Source-bound accuracy (answers must be grounded strictly in book text or user-selected text)
    - Transparency of reasoning (RAG citations must be clear and traceable)
    - Reliability (no hallucinations; no invented information)
    - User-centric clarity (answers must be clear for general readers, not technical experts)
    - Safety-first (no harmful, political, or biased interpretations beyond the text)
    - Deterministic behavior (same input → consistent answer)
Added sections:
- Key Standards
- Constraints
- Operational Rules
- Success Criteria
- Output Quality Benchmarks
Removed sections:
- [PRINCIPLE_6_NAME]
- [PRINCIPLE__DESCRIPTION]
- [SECTION_2_NAME]
- [SECTION_2_CONTENT]
- [SECTION_3_NAME]
- [SECTION_3_CONTENT]
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ updated
- CLAUDE.md ✅ updated
Follow-up TODOs: None
-->
# Interactive RAG-Powered Book (OpenAI Agents + SpecifyKit + Claude CLI) Constitution

## Core Principles

### I. Source-bound accuracy
Answers must be grounded strictly in book text or user-selected text.

### II. Transparency of reasoning
RAG citations must be clear and traceable.

### III. Reliability
No hallucinations; no invented information.

### IV. User-centric clarity
Answers must be clear for general readers, not technical experts.

### V. Safety-first
No harmful, political, or biased interpretations beyond the text.

### VI. Deterministic behavior
Same input → consistent answer.

## Key Standards

### Retrieval Discipline
- If user highlights text: ONLY answer from highlighted text.
- If user asks general question: answer from full book corpus embedded in Qdrant.
- If no relevant text retrieved: say “No supporting information found in the book.”

### RAG Response Structure
- Short summary answer (max 4 lines)
- Supporting evidence (quoted from book)
- Citation ID (Qdrant vector reference key)

### Allowed Knowledge
- Only content present in the book.
- No external facts, no guessing, no assumptions.

### Data Governance
- All chunks must map to Neon Postgres metadata rows.
- Every AI output must reference correct chunk_id(s).

### Writing Style Guidelines
- Grade level: Flesch-Kincaid 8–10 (simple, clear)
- Tone: Neutral, educational, supportive
- Format: short paragraphs, bullet points when possible

## Constraints

- Chatbot must refuse to answer anything outside the book scope.
- Maximum answer length: 200 tokens unless user explicitly requests a longer explanation.
- No hallucinated citations; if retrieval fails, respond safely.
- All internal reasoning must follow SpecifyKit Task → Agent → Contract structure.

## Operational Rules

- Always perform RAG first before answering.
- If user selects text, bypass full retrieval and use ONLY that text.
- If selected text is < 10 characters, fallback to normal RAG.

## Success Criteria

- 100% answers grounded in book’s actual text
- Zero hallucinations in testing
- Latency under 1.5 seconds per query (FastAPI + Qdrant hybrid search)
- All answers include book-based citations
- Smooth integration with SpecifyKit + Claude CLI workflows

## Output Quality Benchmarks

- Accuracy: Must match source text exactly
- Relevance: Only content that answers the user’s question
- Clarity: Understandable by non-technical readers
- Consistency: Identical input → identical answer every time

## Governance

All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance

**Version**: 0.1.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06