# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal portfolio website built with Flask + SQLAlchemy, rendering server-side Jinja2 templates. The entire backend lives in `app.py` (~60 lines). It is an early-stage learning project.

## Commands

Dependencies are managed with **uv** (note `uv.lock` and `pyproject.toml`; `requires-python >=3.12`). Ignore the `pip` / `requirements.txt` / `venv` instructions in the README and planning docs — those predate the switch to uv.

```powershell
uv sync                # install/sync dependencies into .venv
uv run python app.py   # run the dev server at http://localhost:5000 (debug=True)
uv add <package>       # add a dependency (updates pyproject.toml + uv.lock)
```

`app.py` calls `db.create_all()` on startup, so the SQLite DB is created automatically — there is no separate migration/init step.

There are no tests, linters, or build steps configured yet.

## Architecture

- **`app.py`** is the real application and single source of truth: app config, the `ContactMessage` model, a `current_year` context processor, and all routes (`/`, `/about`, `/projects`, `/contact`). The contact route is the only one with `POST` handling and DB writes.
- **`main.py`** is the leftover `uv init` stub (`print("Hello...")`) and is unrelated to the website. The web app entry point is `app.py`, not `main.py`.
- **Database**: SQLite via Flask-SQLAlchemy, file at `instance/personal_website.db` (Flask's default instance folder). The only model is `ContactMessage`.
- **`SECRET_KEY`** is loaded from `.env` via python-dotenv. `.env` is gitignored; the app reads it at import time.
- **Templates** (`templates/`) use Jinja2 inheritance from `base.html`. **`static/css/style.css`** holds custom styles.

## Important: docs describe a plan, not the code

The Markdown files (`PROJECT_PLAN.md`, `ARCHITECTURE.md`, `WEEK_BY_WEEK.md`, `DEPLOYMENT_GUIDE.md`, `README.md`, `VISUAL_REFERENCE.md`, `INDEX.md`) are an aspirational 2-week build plan. They describe features and files that **do not exist yet** — e.g. blog/admin/user models, `config.py`, a `database/` package, `/blog` and `/admin` routes, Render.com deployment (`Procfile`, `gunicorn`). Treat them as a roadmap, not a description of current state. When something there conflicts with `app.py`, `app.py` wins.
