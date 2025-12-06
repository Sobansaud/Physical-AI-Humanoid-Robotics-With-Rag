# Data Model: Physical AI Textbook Frontend

**Date**: 2025-12-04

This document outlines the key entities and their properties for the Physical AI Textbook Frontend. Given this is a static Docusaurus site, these entities primarily represent the structure of content and UI elements rather than dynamic data models.

## 1. Chapter

Represents a main section of the textbook, delivered as an MDX file.

-   **Fields**:
    -   `id`: string (e.g., "01-robotic-nervous-system") - Unique identifier for the chapter, used in URLs.
    -   `title`: string (e.g., "The Robotic Nervous System (ROS 2)") - Display title of the chapter.
    -   `content`: MDX string - The full content of the chapter, including text, code blocks, and interactive elements.
    -   `wordCount`: number - The total number of words in the `content`. (Validation: Must be 700-800 words).
    -   `metadata`: object - Additional information like `tags`, `keywords` for SEO, or `authors`.

-   **Relationships**:
    -   Referenced by `SidebarItem` for navigation.
    -   Can contain various `UI Component` elements within its `content`.

-   **Validation Rules**:
    -   `wordCount` must be between 700 and 800.
    -   `content` must be 100% unique and professionally written (no plagiarism).
    -   `content` must include relevant code examples (e.g., ROS 2).

## 2. Page

Represents a dedicated content section outside of the main chapters (e.g., Learning Outcomes, Weekly Breakdown, Assessments, Hardware Requirements).

-   **Fields**:
    -   `id`: string (e.g., "learning-outcomes") - Unique identifier for the page, used in URLs.
    -   `title`: string (e.g., "Learning Outcomes") - Display title of the page.
    -   `content`: MDX string - The full content of the page, structured according to its specific purpose (e.g., timeline for Weekly Breakdown, rich tables for Hardware Requirements).
    -   `metadata`: object - Optional additional information.

-   **Relationships**:
    -   Referenced by `NavbarItem` and `SidebarItem` for navigation.
    -   Can contain various `UI Component` elements within its `content`.

-   **Validation Rules**:
    -   `content` must be unique and expanded as per the feature specification.
    -   `Weekly Breakdown` content must be presented as a timeline/table layout.
    -   `Hardware Requirements` content must include rich tables and expandable sections.

## 3. UI Component

Represents reusable visual elements used across the site.

-   **Types of Components (Examples)**:
    -   `NavbarItem`: Represents a link in the main navigation.
        -   `label`: string
        -   `to`: string (URL path)
    -   `SidebarItem`: Represents an entry in the collapsible sidebar TOC.
        -   `label`: string
        -   `to`: string (URL path) or `items`: array of `SidebarItem` (for hierarchy)
    -   `ThemeToggle`: Button for switching between dark/light modes.
        -   `state`: enum {`light`, `dark`} (Persistent via `localStorage`).
        -   `animation`: Framer Motion transition.
    -   `ChatbotPlaceholder`: Fixed sidebar widget.
        -   `inputBox`: string (user input area).
        -   `responseDisplay`: string (stubbed API response display).
        -   `selectionSupport`: boolean (supports `window.getSelection()`).
    -   `PageContainer`: Wrapper for doc pages.
        -   `children`: ReactNode (content to be wrapped).
        -   `styles`: object (enforces book margins, subtle page shadow).
    -   `ChapterPreviewCard`: Visual card for home page chapter previews.
        -   `title`: string
        -   `description`: string
        -   `link`: string (to chapter page)

-   **Relationships**:
    -   Integrated into `docusaurus.config.js` (for navbar/footer) and `sidebars.js`.
    -   Used within `Chapter` and `Page` MDX content or React layouts.

-   **Validation Rules**:
    -   `ThemeToggle` must provide instant, seamless switching and persist selection.
    -   `ChatbotPlaceholder` must be fixed, and support `window.getSelection()` for selected text highlighting.
    -   `PageContainer` must correctly apply book margins and page shadow.
    -   All components must be fully responsive and adhere to accessibility standards (WCAG 2.1 AA).

## 4. Configuration (Implicit Entities)

Though not explicit data models, `docusaurus.config.js` and `sidebars.js` act as critical configuration entities that define the site's structure, theme, and navigation.

-   **`docusaurus.config.js`**: Defines global site metadata, navbar, footer, theme configuration, presets, and custom CSS.
-   **`sidebars.js`**: Defines the hierarchical and collapsible structure of the sidebar navigation for documentation.