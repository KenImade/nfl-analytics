FROM python:3.13-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:0.10.7 /uv /uvx /bin/

COPY . /app

ENV UV_NO_DEV=1

WORKDIR /app
RUN uv sync --locked

CMD [ "uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]

