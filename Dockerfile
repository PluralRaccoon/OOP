# -- Stage 1 Builder --
FROM python:3.10-slim AS builder
WORKDIR /caja
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock .
RUN poetry config virtualenvs.in-project true && \
    poetry install --only types --no-root --no-interaction --no-ansi
    
# -- Stage 2 Runtime --
FROM python:3.10-slim AS runtime
RUN groupadd -r python && useradd -r -g python bot
WORKDIR /caja
COPY --from=builder --chown=bot:python /caja/.venv ./.venv
COPY --chown=bot:python src/main.py .
USER bot
VOLUME ["/caja/madriguera"]
ENTRYPOINT ["python", "main.py"]
