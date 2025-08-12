# Use a small official Python image
FROM python:3.11-slim

# Set working dir
WORKDIR /app

# System deps (if you need build tools uncomment)
# RUN apt-get update && apt-get install -y build-essential

# Copy only requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Make port consistent with ECS/container expectation
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

# Run gunicorn (adjust workers to your app)
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000", "--workers", "3", "--threads", "2"]
