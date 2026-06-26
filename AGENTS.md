# AGENTS.md

Repository-specific instructions for AI coding agents working in this project.

## Scope

- Work only inside `/Users/aravindshaj/research/coursework/llm-foundations`.
- Do not read `~/private-keys`, `~/.ssh`, `~/.config/gh`, or any files outside this repository.
- Do not modify, commit, or push files outside this repository.

## Secrets and Credentials

- Never print, request, store, or commit secrets.
- Never commit `.env` files, tokens, API keys, credentials, private key files, or W&B, Hugging Face, or GitHub tokens.
- Treat any secret-like value as sensitive even if it appears in local files or command output.
- If a secret appears in a diff or tracked file, stop and report it before taking further action.

## Git Workflow

- Do not commit or push unless explicitly asked by the repository owner.
- Before any commit, run:
  - `git status`
  - `git diff --staged`
- Keep commits focused and avoid mixing unrelated changes.
- Do not rewrite history, reset branches, or discard user changes unless explicitly instructed.

## Development Workflow

- Use Python 3.
- Use PyTorch for tensor and model work.
- Use `pytest` for tests.
- Use `ruff` for linting and formatting checks.
- Prefer small, readable, testable code.
- Follow the existing repository structure:
  - `notes/` for learning notes and daily logs
  - `from_scratch/` for PyTorch implementations
  - `notebooks/` for Colab, Kaggle, or Jupyter notebooks
  - `paper_summaries/` for short paper summaries

## Quality Bar

- Make narrow, intentional changes that directly support the task.
- Add or update tests when behavior changes.
- Prefer explicit names and simple control flow over clever abstractions.
- Keep generated outputs, datasets, checkpoints, caches, and local environment files out of git.
