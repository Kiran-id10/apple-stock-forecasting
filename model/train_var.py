import pandas as pd
from statsmodels.tsa.api import VAR
import joblib

df = pd.read_csv("data/df_finals.csv")

# KEEP ONLY REQUIRED FEATURES
df = df[["stock_price", "sp500_index", "market_sentiment"]]

# 🔥 IMPORTANT: DIFFERENCING (THIS IS THE MISSING PIECE)
df_diff = df.diff().dropna()

# Train VAR
model = VAR(df_diff)
results = model.fit(maxlags=5)

# Save model
joblib.dump(results, "model/var_model.pkl")

# Save last original value for reconstruction
joblib.dump(df.iloc[-1], "model/last_values.pkl")

print("✅ Model trained correctly")
