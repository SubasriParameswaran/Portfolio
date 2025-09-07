import argparse
import json
from pathlib import Path
import joblib
import numpy as np

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "model.pkl"

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Train it first.")
    bundle = joblib.load(MODEL_PATH)
    return bundle["model"], bundle["feature_names"]

def main():
    parser = argparse.ArgumentParser(description="Predict with the trained model")
    parser.add_argument("--input", type=str, required=True, help="Path to JSON file with feature:value mapping")
    args = parser.parse_args()

    model, feature_names = load_model()
    with open(args.input, "r") as f:
        payload = json.load(f)

    # Ensure correct order + missing feature check
    X = []
    for name in feature_names:
        if name not in payload:
            raise ValueError(f"Missing feature: {name}")
        X.append(payload[name])
    X = np.array(X).reshape(1, -1)

    pred = model.predict(X)[0]
    print(json.dumps({"prediction": float(pred)}, indent=2))

if __name__ == "__main__":
    main()
