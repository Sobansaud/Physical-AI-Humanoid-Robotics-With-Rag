---
id: 1
title: Update project constitution with core principles
stage: constitution
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["constitution", "initialization", "principles"]
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

Project: AI/Spec-Driven Professional Textbook Frontend on "Physical AI & Humanoid Robotics: The Future of Embodied Intelligence" (Docusaurus 3.9 + GitHub Pages Deployment)

Core Principles and Immutable Standards:
- All development must be rigorously Spec-Driven using Spec-Kit Plus: Every aspect of the frontend, including content generation, layout design, component implementation, and styling, must originate from clear, testable specifications. No ad-hoc changes or implementations are permitted; specifications must explicitly define intent, success criteria, constraints, non-goals, and acceptance tests prior to any coding or content creation. This ensures traceability, reusability, and alignment with project requirements for high-quality, error-free deliverables.
- Premium and Engaging User Experience: The website must deliver a sophisticated aesthetic that is visually compelling, intuitive, and immersive, positioning it as a high-quality educational resource. Incorporate purple-to-cyan gradients (#6A1B9A to #00FFFF) for backgrounds and accents, glassmorphism effects (semi-transparent blurred cards with borders and shadows) for chapter sections and sidebars, Framer Motion for fluid animations (e.g., smooth page transitions, fade-ins on scroll, hover effects like subtle glows or particle bursts on interactive elements), and a mobile-first responsive design ensuring seamless viewing on all devices (with 100% Lighthouse mobile scores).
- Accessibility Excellence: Adhere strictly to WCAG 2.1 AA standards, including ARIA labels on all interactive elements (e.g., navigation items, toggle buttons), keyboard navigation support with visible focus states, alt text for all images/icons, and high contrast ratios (minimum 4.5:1 for text). Semantic HTML must be used throughout (e.g., <article> for chapters, <nav> for sidebar), and test with screen readers to ensure full usability for diverse audiences.
- Performance Optimization: The site must achieve exceptional load times (First Contentful Paint <1.5 seconds, bundle size <500KB after optimization), utilizing lazy loading for images and sections, code splitting for routes, and efficient asset management (e.g., optimized fonts via Google Fonts or self-hosted, compressed images). No performance bottlenecks allowed; conduct audits at each phase.
- Content Integrity and Professionalism: All textbook content must be generated with professional, error-free language, drawing directly from the provided document's structure (e.g., modules, learning outcomes, weekly breakdown, assessments, hardware requirements). Content must be original, factually accurate, and optimized for readability (Flesch-Kincaid grade 10-12), with no plagiarism. Use MDX for interactive elements (e.g., code blocks for ROS 2 examples).

Quality Standards and Testable Criteria:
- Content Structure: The site must feature a home page with book introduction and overview; 5-7 main chapters mirroring the document's modules (Module 1: The Robotic Nervous System (ROS 2), Module 2: The Digital Twin (Gazebo & Unity), Module 3: The AI-Robot Brain (NVIDIA Isaac™), Module 4: Vision-Language-Action (VLA)), each 700-800 words in MDX format with sub-sections; dedicated pages/sections for Learning Outcomes, Weekly Breakdown (Weeks 1-13), Assessments, and Hardware Requirements (including detailed breakdowns of workstations, edge kits, robot labs, and cloud options). All sections must include headings, bullet points, tables (e.g., for hardware costs), and code snippets where relevant (e.g., ROS 2 examples).
- UI/UX Standards: Implement a collapsible sidebar TOC for navigation with smooth scrolling; dark/light mode toggle (persistent via localStorage, with seamless theme switching); search functionality for content; and interactive elements (e.g., hover animations). Styling must be consistent: Custom theme overrides in `src/css/custom.css`, gradients applied to headers/backgrounds, glassmorphism on content cards (e.g., backdrop-filter: blur(10px), background: rgba(255,255,255,0.1), border: 1px solid rgba(255,255,255,0.18)), and Framer Motion animations (e.g., AnimatePresence for page transitions, motion.div for hover scales/glows).
- Integration Readiness: Include a dedicated React component in the sidebar for future RAG chatbot embed (e.g., placeholder input box with API call stubs), ensuring it supports user-selected text via window.getSelection().
- Success Evals: The site must pass Lighthouse audits with 95+ scores across performance, accessibility, best practices, and SEO; all chapters must be navigable without errors or broken links; styling must render flawlessly on Chrome, Firefox, Safari, and mobile devices (tested via BrowserStack or similar); deployment must succeed with full functionality on GitHub Pages; manual testing of 10+ navigation flows and content searches must yield 100% success.
- Error Handling and Robustness: Implement graceful fallbacks for loading states (e.g., skeletons for content), console logging for debug (no user-facing errors), and comprehensive error boundaries in React components.

Constraints and Non-Negotiables:
- Tools and Dependencies: Docusaurus 3.9 as the core framework (classic template with TypeScript); Claude Code for all content and code generation; Spec-Kit Plus for the full workflow (constitution → specification → clarification → planning → tasks → implementation). Additional: Framer Motion for animations, Tailwind CSS for utilities (if needed for custom styles). No heavy external libraries; free tools only (no paid APIs or services).
- Timeline and Phasing: Complete by December 4, 2025, evening; structured into phases with mandatory checkpoints after each (e.g., review content accuracy before styling). Ensure methodical progression without haste.
- Non-Goals: No backend integration in this frontend phase (chatbot calls will be stubbed); no video embeds, user authentication, or dynamic content beyond static MDX and basic interactions; avoid over-complexity—focus on clean, premium design without unnecessary features.
- Ethical and Compliance Standards: Content must be original and aligned with the provided document; ensure no biased or inaccurate information on hardware/AI topics.

Governance and Workflow Rules:
- This constitution is the foundational, immutable document governing all frontend development; all subsequent specifications, plans, and tasks must inherit and respect these rules without exception.
- Workflow Cascade: Follow Spec-Kit Plus phases strictly—begin with specification refinement, proceed to planning, break into atomic tasks (15-30 minutes each), implement with AI collaboration and checkpoints.
- Version Control and Traceability: Use Git for all changes; commit after each phase with conventional commit messages (e.g., "feat: add chapter content"); maintain full traceability from specs to code via comments and history folders.
- Review and Iteration Process: At each checkpoint, conduct manual verification against success criteria; iterate immediately if standards are not met (e.g., refine content for readability); no proceeding without explicit approval.
- Collaboration with AI: All prompts to Claude Code must be detailed, context-rich, and optimized for professional output.

## Response snapshot

The project constitution has been successfully updated to version 1.0.0. This is a minor version bump due to the addition of core principles and new sections.

Manual follow-up is required for the following template files:
- `.specify/templates/plan-template.md`: The "Constitution Check" section needs to be updated to align with the new principles.
- `.specify/templates/spec-template.md`: Ensure that spec creation aligns with the new constitutional principles, especially the "Quality Standards and Testable Criteria" and "Constraints and Non-Negotiables".
- `.specify/templates/tasks-template.md`: Ensure that task categorization and test definitions align with the new constitutional principles.

Suggested commit message:
`docs: amend constitution to v1.0.0 (initial creation with core principles and governance)`

## Outcome

- ✅ Impact: Constitution updated with core principles and governance rules.
- 🧪 Tests: N/A
- 📁 Files: Modified 1 file: .specify/memory/constitution.md
- 🔁 Next prompts: "Update .specify/templates/plan-template.md, .specify/templates/spec-template.md, and .specify/templates/tasks-template.md to align with the new constitution."
- 🧠 Reflection: The constitution was successfully updated, but dependent templates require manual updates to ensure consistency.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
