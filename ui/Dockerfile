# ui/Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY ./ui /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["streamlit", "run", "sum_app.py", "--server.port=8501", "--server.address=0.0.0.0"]