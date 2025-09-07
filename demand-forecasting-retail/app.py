from pathlib import Path

import joblib
import numpy as np
import streamlit as st

st.title("Retail Demand Forecasting — Demo App")

MODEL_PATH = Path(__file__).resolve().parents[0] / "models" / "model.pkl"


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(
            "Model not found. Please run `python src/train.py` first to create models/model.pkl"
        )
        st.stop()
    bundle = joblib.load(MODEL_PATH)
    return bundle["model"], bundle["feature_names"]


model, feature_names = load_model()

st.write("Input features:")
values = {}
cols = st.columns(3)
for i, name in enumerate(feature_names):
    with cols[i % 3]:
        values[name] = st.number_input(name, value=0.0)

X = np.array([values[n] for n in feature_names]).reshape(1, -1)
if st.button("Predict"):
    yhat = model.predict(X)[0]
    st.success(f"Predicted demand: {yhat:.2f}")
