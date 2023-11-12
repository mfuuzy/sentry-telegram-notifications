FROM python:3.11-slim-bookworm
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "/app/main.py"]
