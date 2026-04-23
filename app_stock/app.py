from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI()

var_model = joblib.load("model/var_model.pkl")
last_values = joblib.load("model/last_values.pkl")

@app.post("/predict")
def predict(data: dict):
    try:
        input_data = np.array(data["input"], dtype=float)

        # DIFFERENCE INPUT (same as training)
        input_diff = np.diff(input_data, axis=0)

        # Use last k_ar rows
        input_diff = input_diff[-var_model.k_ar:]

        forecast_diff = var_model.forecast(input_diff, steps=30)

        # 🔥 RECONSTRUCT ORIGINAL VALUES
        forecast = []
        last_stock = last_values["stock_price"]

        for step in forecast_diff:
            last_stock = last_stock + step[0]
            forecast.append(float(last_stock))

        return {"forecast": forecast}

    except Exception as e:
        return {"error": str(e)}
