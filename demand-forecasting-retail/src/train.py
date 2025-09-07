import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sales.csv"
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "model.pkl"


def main():
    if not DATA_PATH.exists():
        print(
            f"[!] Expected data at {DATA_PATH}. "
            "Please add a 'sales.csv' with numeric features and a 'target' column."
        )
        return

        df = pd.read_csv(DATA_PATH)
        if "target" not in df.columns:
            raise ValueError("Your data must contain a 'target' column for the value to predict.")

        X = df.drop(columns=["target"])
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump({"model": model, "feature_names": list(X.columns)}, MODEL_PATH)

        print(json.dumps({"mse": mse, "r2": r2, "test_size": len(X_test)}, indent=2))


if __name__ == "__main__":
    main()
