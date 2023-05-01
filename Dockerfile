FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
COPY watch_next.py .
COPY movies.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "watch_next.py"]

