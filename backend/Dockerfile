FROM python:3.12.3-slim

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY scripts/start_prod.sh /start_prod.sh

COPY . .

RUN python manage.py collectstatic --noinput