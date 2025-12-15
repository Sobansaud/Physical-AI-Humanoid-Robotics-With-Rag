FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for cache efficiency
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code
COPY app ./app

# Expose the port expected by HF Spaces (7860) and uvicorn
EXPOSE 7860

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
