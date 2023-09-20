FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR copy/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .