# Use Python 3.11 slim image
FROM python:3.11-slim

# Install curl and system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

COPY ./src /app/src
COPY ./app_data /app/app_data

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

