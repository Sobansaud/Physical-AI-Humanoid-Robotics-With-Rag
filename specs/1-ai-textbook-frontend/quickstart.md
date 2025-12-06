# Quickstart Guide: Physical AI Textbook Frontend

**Date**: 2025-12-04

This guide provides instructions to set up and run the "Physical AI Textbook Frontend" Docusaurus project locally.

## Prerequisites

Ensure you have the following installed on your system:

-   Node.js (LTS version, e.g., 18.x or 20.x)
-   npm (Node Package Manager)
-   Git

## Project Setup

1.  **Clone the Repository**:

    First, ensure you have cloned the main project repository. If you haven't already, run:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Navigate to the Docusaurus Project Directory**:

    The Docusaurus project (`physical-ai-textbook`) is located within the main repository. Navigate into it:

    ```bash
    cd physical-ai-textbook
    ```

3.  **Install Dependencies**:

    Install all required Node.js packages, including Docusaurus, Framer Motion, and Tailwind CSS. The initial `npx create-docusaurus` command might have already done some of this, but it's good practice to ensure all are installed.

    ```bash
    npm install
    ```

    Additionally, install the specific dependencies for this project as per Phase 1, Step 2 of the plan:

    ```bash
    npm install framer-motion tailwindcss postcss autoprefixer @docusaurus/theme-live-codeblock
    ```

4.  **Initialize Tailwind CSS**:

    Initialize Tailwind CSS within the Docusaurus project. This will create a `tailwind.config.js` and `postcss.config.js` file.

    ```bash
    npx tailwindcss init -p
    ```

## Running the Project

### 1. Start Development Server

To start the local development server and view the site in your browser, run:

```bash
npm start
```

This will open the site at `http://localhost:3000` (or another available port) in your default web browser.

### 2. Build for Production

To build the static files for production deployment, run:

```bash
npm run build
```

The built static assets will be located in the `build/` directory.

### 3. Deploy to GitHub Pages

To deploy the built site to GitHub Pages, run:

```bash
npm run deploy
```

**Note**: Ensure your `docusaurus.config.js` is correctly configured for GitHub Pages deployment (e.g., `url`, `baseUrl`).

## Project Structure

Key directories and files:

-   `docs/`: Contains all Markdown/MDX content for chapters and dedicated pages.
-   `src/`: Contains custom React components, CSS, and theme overrides.
    -   `src/css/custom.css`: Global styles.
    -   `src/components/`: Custom UI components like `ChatbotPlaceholder.tsx`, `ThemeToggle.tsx`, `PageContainer.tsx`.
    -   `src/theme/Root.js`: Integrates Framer Motion.
-   `docusaurus.config.js`: Main Docusaurus configuration.
-   `sidebars.js`: Defines the documentation sidebar structure.