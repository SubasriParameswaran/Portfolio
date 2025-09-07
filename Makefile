setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r templates/requirements.txt && pre-commit install

lint:
	ruff check .
	black --check .

test:
	pytest -q

run-app:
	streamlit run demand-forecasting-retail/app.py
