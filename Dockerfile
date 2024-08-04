FROM python:3.12-slim
LABEL authors="adnrey"

USER root

ENV ENV_FILE=$ENV_FILE
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip "poetry==1.8.3"
RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./
RUN poetry install --without dev

WORKDIR /src

COPY src .

CMD hypercorn main:app --bind 0.0.0.0:12000
