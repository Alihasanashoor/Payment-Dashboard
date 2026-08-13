FROM python:3.11

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \ 
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]