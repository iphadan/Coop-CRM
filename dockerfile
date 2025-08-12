FROM python:3.12.9-slim-bookworm

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure output is flushed directly (no buffering)
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

# Upgrade pip (typo fixed)  
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

# Correct CMD syntax
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
