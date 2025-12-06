FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for cache efficiency
# Assuming Dockerfile is in 'back/' and requirements in 'back/backend/'
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code
COPY backend ./backend

# Expose the port expected by HF Spaces (7860) and uvicorn
EXPOSE 7860

# Run the application
# We are in /app, so backend package is at /app/backend
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "7860"]
