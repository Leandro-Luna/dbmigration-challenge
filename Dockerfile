FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt ./app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt

WORKDIR /app

COPY . .
