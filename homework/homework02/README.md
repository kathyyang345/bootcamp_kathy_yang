# Homework 02 — Tooling Setup

## What I practiced

In this assignment, I built a reproducible project scaffold for the first time — this is meant to mirror the structure I'll use for real in `project/` later on. I created a dedicated conda environment (`fe-course`, Python 3.11) and installed `python-dotenv`, `numpy`, and `jupyter` inside it, so this homework doesn't depend on whatever happens to be in my base environment. I set up secret management with a `.env` file (kept out of Git via `.gitignore`) and a matching `.env.example` template that documents the expected keys without exposing real values. I wrote a small `src/config.py` helper with `load_env()` and `get_key()` functions so that any notebook or script in this project can load configuration the same way, instead of repeating `dotenv` boilerplate everywhere. Finally, I verified everything works end-to-end in `notebooks/00_project_setup.ipynb`: the notebook confirms `API_KEY` is loaded correctly from `.env` and runs a short NumPy demo. I also froze the environment with `pip freeze > requirements.txt` so this setup can be reproduced exactly by anyone (including future me).

## Environment

- Created with: `conda create -n fe-course python=3.11 -y`
- Activated with: `conda activate fe-course`
- Packages installed: `python-dotenv`, `numpy`, `jupyter` (see `requirements.txt` for exact pinned versions)