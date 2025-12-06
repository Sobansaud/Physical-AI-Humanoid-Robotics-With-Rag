# API Contracts

**Date**: 2025-12-04

This `contracts/` directory is part of the Spec-Kit Plus planning workflow. For this project, the "Physical AI Textbook Frontend," a formal API contract (e.g., OpenAPI or GraphQL schema) is not generated for the following reasons:

1.  **Static Site**: The project is implemented as a static Docusaurus website. It primarily serves pre-rendered content and does not interact with a dynamic backend or expose its own APIs in the traditional sense.
2.  **No Backend Integration (Non-Goal)**: The feature specification explicitly states "No backend" as a non-goal for this phase. All content is static, and interactive elements are handled client-side or stubbed.

## Chatbot Placeholder API Interaction (Stubbed)

The only component that *would* interact with an external API in a real-world scenario is the `ChatbotPlaceholder`. As per the specification, this component will implement a "stub API call with console.log".

-   **Endpoint (conceptual)**: `/api/chatbot/query` (or similar)
-   **Method**: `POST`
-   **Request Body (conceptual)**:
    ```json
    {
        "query": "string",
        "context": "string" // User-selected text from window.getSelection()
    }
    ```
-   **Response Body (conceptual)**:
    ```json
    {
        "response": "string"
    }
    ```
-   **Implementation**: For this project, this will be simulated client-side (e.g., `console.log` the query and context, return a dummy response). No actual network requests will be made in this phase.

If a backend were to be integrated in a future phase, this directory would then contain the formal API schemas for all exposed endpoints.