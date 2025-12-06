# Deployment Guide: URL Configuration

**Current Status:**
-   ✅ **Frontend URL (Deployed):** `https://physical-ai-humanoid-robotics-new.vercel.app`
-   ⚠️ **Backend URL (Pending):** You need to deploy the backend to get this URL.

---

## 1. Backend Configuration (Done)

I have updated `backend/app/main.py` to allow requests from your deployed frontend.

**Current Settings in `main.py`:**
```python
allow_origins=[
    "*",
    "http://localhost:3000",
    "https://physical-ai-humanoid-robotics-new.vercel.app"
]
```

---

## 2. Frontend Configuration (Action Required after Backend Deployment)

Once you deploy this backend (e.g., to Hugging Face Spaces), you will get your **Backend URL**. You must update the frontend code to use it.

### **File to Update:**
`physical-ai-textbook/src/components/ChatbotComponent.tsx`

### **Steps:**
1.  Get your new Backend URL (e.g., `https://huggingface.co/spaces/your-username/your-space-name/api`).
2.  Open `physical-ai-textbook/src/components/ChatbotComponent.tsx`.
3.  Replace `http://localhost:8000` with your **new Backend URL**.

**Search and Replace:**
-   Find: `http://localhost:8000/api/ask`  ->  Replace with: `https://<YOUR_BACKEND_URL>/api/ask`
-   Find: `http://localhost:8000/api/ask-selection` -> Replace with: `https://<YOUR_BACKEND_URL>/api/ask-selection`

---
