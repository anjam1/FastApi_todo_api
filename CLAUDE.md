# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based Todo application. The project is in its early stages with minimal structure. It uses Python 3.12+ and uv for dependency management.

## Development Environment

- **Python version**: 3.12 (specified in `.python-version`)
- **Package manager**: uv (uses `pyproject.toml` and `uv.lock`)
- **Virtual environment**: `.venv` (excluded in `.gitignore`)

## Common Development Tasks

### Setting up the development environment
```bash
# Install dependencies using uv
uv sync
```

### Running the application
```bash
# Start the FastAPI development server
uv run fastapi dev main.py
```

### Alternative: Run with uvicorn directly
```bash
uv run uvicorn main:app --reload
```

### Accessing the API
- The application runs on `http://localhost:8000` by default
- API documentation is available at `http://localhost:8000/docs` (Swagger UI) and `http://localhost:8000/redoc` (ReDoc)

## Project Structure

The project currently has a minimal structure:
- `main.py`: Main FastAPI application with a single root endpoint
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Locked dependencies for reproducible builds
- `.python-version`: Specifies Python 3.12
- `.gitignore`: Standard Python gitignore patterns

## Dependencies

The main dependency is:
- `fastapi[standard]>=0.128.7`: Includes FastAPI with standard extras (uvicorn, pydantic, etc.)

## Architecture Notes

1. **Current State**: The application has only a basic root endpoint returning a welcome message.
2. **Future Expansion**: This appears to be the starting point for a Todo application. Future development would likely include:
   - Todo item models (Pydantic schemas)
   - CRUD endpoints for todo operations
   - Database integration (SQLAlchemy, asyncpg, etc.)
   - Authentication/authorization
   - Frontend integration or API-only design

## Git Workflow

- The repository uses `master` as the current branch (not `main`)
- No specific branching strategy is established yet

## Important Notes

- The project uses uv for dependency management, not pip
- The virtual environment `.venv` is gitignored
- No testing framework or CI/CD configuration is currently set up
- No database or data persistence layer is implemented yet