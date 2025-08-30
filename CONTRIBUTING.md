# Contributing to HeritageVerse

Thanks for your interest in contributing! This guide helps you set up a dev environment, follow coding standards, and submit changes smoothly.

## Getting Started
1. **Fork** the repo and **clone** your fork.
2. Create a virtualenv and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Create a feature branch:
   ```bash
   git checkout -b feat/<short-description>
   ```

## Development Guidelines
- **Code style:** Follow Python best practices; keep functions small and well‑named.
- **Type hints:** Use when helpful.
- **Logging & errors:** Surface clear user‑facing messages in Streamlit. Fail gracefully on network/MEGA issues.
- **Secrets:** Never commit credentials. Use env vars (`MEGA_EMAIL`, `MEGA_PASSWORD`).

## Commit Messages
Use **Conventional Commits**:
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation only
- `refactor:` code change that neither fixes a bug nor adds a feature
- `chore:` tooling or maintenance

Example:
```
feat(tts): add fallback handling when gTTS lang unsupported
```

## Branching & PRs
- Branch from `main`.
- Keep PRs small and focused.
- Link issues (e.g., "Closes #12").
- Fill the PR checklist:
  - [ ] Code builds locally
  - [ ] No secrets committed
  - [ ] Tested manually (low-bandwidth scenario)
  - [ ] Docs updated (README/CHANGELOG if needed)

## Issue Reporting
Open an issue with:
- Expected behavior
- Actual behavior & logs
- Steps to reproduce
- Environment details (OS, Python version)

## Code of Conduct
Be respectful. Focus on constructive feedback. Harassment or discrimination is not tolerated.
