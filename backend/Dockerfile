FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 0
ENV PYTHONUNBUFFERED 0

WORKDIR /code

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock /code/
RUN poetry install --no-root

COPY ./app /code/app
COPY ./alembic /code/alembic
COPY ./alembic.ini /code/alembic.ini
COPY ./scripts /code/scripts

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
