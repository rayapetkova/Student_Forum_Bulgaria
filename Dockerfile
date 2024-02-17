FROM python:3.13.0a4-slim-bullseye


WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

