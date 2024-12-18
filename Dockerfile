FROM python:3.11-slim

RUN apt-get update && apt-get install -y tree

WORKDIR /app


RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000