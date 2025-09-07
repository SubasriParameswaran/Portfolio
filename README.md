# Data Science & ML Portfolio Starter

This repo is a **starter kit** to jumpstart your GitHub portfolio. It includes:
- A **profile README** template to showcase your story.
- A reusable **project template** (README, CI, pre-commit, env).
- Two example, career-relevant projects for you to complete and publish.
- A minimal **CI workflow** and **code quality** setup to look professional.

> Generated for **Suba Parameswaran** on **2025-09-07**. Replace placeholders with your details, then push to GitHub.

## How to use
1. Create a new GitHub repo (e.g., `suba-portfolio`) and clone it.
2. Copy the pieces you want from this starter. Or initialize this directory as your portfolio repo.
3. Replace `your-github-username` with your GitHub username in links.
4. Start with `demand-forecasting-retail` (flagship project), then ship the rest.
5. Turn each project into its **own repo** once polished, and **pin** the best 6 on your profile.

## Quick commands
```bash
# optional: create a virtual environment
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install tools used by this starter
pip install -r templates/requirements.txt
pip install pre-commit

# enable quality gates for your local repo
pre-commit install

# run linters / tests
ruff check .
black --check .
pytest -q

# run the demo app example (after training a model)
streamlit run demand-forecasting-retail/app.py
```

## What’s inside
- `PROFILE_README/README.md` → your **profile** landing page content.
- `templates/` → reusable files: project README template, CI, pre-commit, etc.
- `demand-forecasting-retail/` → your **flagship DS/ML** project (joblib model + Streamlit app).
- `inventory-optimization-eoq/` → quick **operations research** project.
- `powerbi-vendor-performance/` → **Power BI** measures and write-up for vendor performance.

---
**Tip:** Keep real datasets out of the repo. Use small samples or provide instructions to download from public sources.
