FROM python:3.10-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy application code into the container
COPY . /app

# Install dependencies and lock them
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the FastAPI app
CMD ["uv", "run", "fastapi", "run"]