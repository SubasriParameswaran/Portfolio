# <Project Title>

> One line: who is this for and what decision does it improve?

## 1) Problem
- Business context and KPI (e.g., forecast error, stockouts, SLA).
- Why now? What happens if we don’t solve it?

## 2) Data
- Source(s), size, timespan, key fields.
- Assumptions & data cleaning steps.
- **Privacy**: how sensitive data is handled. Use synthetic or public data if needed.

## 3) Method
- Baseline (naïve / rule-based), then ML.
- Feature engineering highlights (what actually helped).
- Models tried and selection criteria.
- Cross-validation, metrics, and error analysis.

## 4) Results
- Compare against baseline.
- Show business translation (e.g., “3.2% better MAPE ≈ $120k/year savings”).
- Visuals (few, focused).

## 5) Demo
- Link to Streamlit / Hugging Face / Colab.
- GIF or screenshot of the app.

## 6) How to run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/train.py
python src/predict.py --input sample_input.json
# optional app
streamlit run app.py
```

## 7) Repo guide
- `data/` (blank, with instructions)
- `notebooks/` (EDA, experiments)
- `src/` (functions, training, inference)
- `models/` (saved artifacts, excluded from git by default)
- `tests/` (a few key tests)

## 8) Learnings & next steps
- What surprised you?
- What would you try next if you had 2x time?
