FROM python:3.11-slim

WORKDIR /bboom_test_app

ENV PYTHONUNBUFFERED=1

COPY poetry.lock pyproject.toml pytest.ini ./
COPY bboom_test/. ./bboom_test
COPY users/. ./users
COPY posts/. ./posts
COPY tests/. ./tests
COPY ui/. ./ui
COPY manage.py .
COPY README.md .

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev