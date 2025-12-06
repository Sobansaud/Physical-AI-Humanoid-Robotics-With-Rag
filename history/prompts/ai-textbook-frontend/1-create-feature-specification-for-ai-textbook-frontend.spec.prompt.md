---
id: 1
title: Create feature specification for AI Textbook Frontend
stage: spec
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: ai-textbook-frontend
branch: 1-ai-textbook-frontend
user: user
command: /sp.specify
labels: ["specification", "frontend", "docusaurus"]
links:
  spec: specs/1-ai-textbook-frontend/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-ai-textbook-frontend/spec.md
  - specs/1-ai-textbook-frontend/checklists/requirements.md
tests:

---

## Prompt

Physical AI Textbook Frontend

Intent:
Build a premium, interactive, and fully responsive textbook website titled
“Physical AI & Humanoid Robotics: The Future of Embodied Intelligence” using Docusaurus 3.9.

The final site must look and feel exactly like a real, professionally published technical book (O’Reilly / Manning level), with clean book-like typography, elegant page layout, realistic margins, subtle page shadows, and a reading comfort that makes judges say “yeh toh asli kitab lag rahi hai”. At the same time, it must have modern premium web enhancements (purple-cyan gradients, glassmorphism, Framer Motion animations, dark/light mode, collapsible TOC).

This entire project is executed inside Claude CLI with Context-7 MCP server fully connected, giving you complete file-system access and terminal execution rights. You have 100% authority to install Docusaurus, generate every single file, run commands, commit, and deploy to GitHub Pages completely autonomously — I will only say “Approved” at checkpoints.

Content Rules (Non-Negotiable):
- Every chapter and every section must contain 100% unique, freshly written, never-seen-before content.
- Do NOT copy-paste from the original document word-for-word. Rewrite everything in a new, richer, more insightful, and highly professional style while keeping all technical facts 100% accurate.
- Expand, explain, add real-world examples, analogies, and deeper insights so the book feels like a brand-new 2025 flagship textbook, not a recycled slide deck.
- Zero plagiarism, zero repetition, zero generic filler — every paragraph must feel fresh and valuable.

Features & Exact Structure:
- Home Page: Hero with title, subtitle, powerful introduction + visual chapter preview cards
- 5 Main Chapters (exactly 700–800 words each, MDX):
  1. The Robotic Nervous System (ROS 2)
  2. The Digital Twin (Gazebo & Unity)
  3. The AI-Robot Brain (NVIDIA Isaac™)
  4. Vision-Language-Action (VLA)
  5. Why Physical AI Matters
- Dedicated Pages (all unique, expanded content):
  • Learning Outcomes (standalone page)
  • Weekly Breakdown (Weeks 1–13, beautiful timeline/table)
  • Assessments
  • Hardware Requirements (rich tables + expandable sections for every option)

Visual & Layout Requirements (must feel like a real book):
- Book-like typography: IBM Plex Serif or Georgia for body, bold modern sans for headings
- Max reading width ~65ch, generous line-height 1.7–1.8, proper page margins (4–6rem on desktop)
- Subtle page shadow / inner border effect on chapter pages
- Collapsible, hierarchical sidebar TOC (always visible on desktop)
- Purple → cyan gradient accents (#6A1B9A → #00FFFF)
- Glassmorphism cards for tables, code, hardware sections
- Framer Motion: page fade-ins, smooth scroll, hover glow + tiny particle burst on titles
- Dark/light mode toggle (instant, persistent)
- Beautiful fixed RAG chatbot placeholder in sidebar (supports selected-text highlighting)

Success Criteria:
- Judges must feel “this is a real published book on the web”
- 100% unique & fresh content (feels brand-new, not copied)
- Lighthouse 95+ across all four categories
- Every chapter exactly 700–800 words
- Zero grammar/plagiarism issues
- Fully responsive (perfect on mobile)
- Live on GitHub Pages, zero broken assets

Constraints & Permissions (CRITICAL):
- Running inside Claude CLI + Context-7 MCP server → full terminal + filesystem access
- You are explicitly authorized to autonomously:
  • npx create-docusaurus@latest
  • npm install framer-motion tailwindcss etc.
  • Create/modify every file
  • git add/commit/push
  • npm run deploy (GitHub Pages)
- Zero manual work from me except “Approved, proceed” at checkpoints

Non-Goals:
- No backend, no videos, no auth, no paid services

This specification inherits every rule from the constitution and commands you to deliver an absolutely unique, breathtaking, real-book-quality masterpiece that will win the hackathon.

## Response snapshot

The feature specification `specs/1-ai-textbook-frontend/spec.md` for the branch `1-ai-textbook-frontend` has been created and validated.
All specification quality checks passed.

## Outcome

- ✅ Impact: Feature specification for "Physical AI Textbook Frontend" created and validated.
- 🧪 Tests: N/A
- 📁 Files: Created specs/1-ai-textbook-frontend/spec.md, specs/1-ai-textbook-frontend/checklists/requirements.md
- 🔁 Next prompts: The feature is ready for the planning phase (run `/sp.plan`).
- 🧠 Reflection: Successfully created a detailed specification based on user input, ensuring all quality checks passed.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
