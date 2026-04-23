import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Apple Stock Forecast", layout="wide")

st.title("📈 Apple Stock Forecast Dashboard")

# -------------------------------
# FILE UPLOAD
# -------------------------------
file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    # -------------------------------
    # REQUIRED COLUMNS
    # -------------------------------
    required_cols = ["stock_price", "sp500_index", "market_sentiment"]

    if not all(col in df.columns for col in required_cols):
        st.error("Dataset must contain: stock_price, sp500_index, market_sentiment")
        st.stop()

    df = df[required_cols].dropna()

    # -------------------------------
    # SHOW HISTORICAL DATA
    # -------------------------------
    st.subheader("📊 Historical Stock Price")

    fig_hist, ax_hist = plt.subplots(figsize=(12, 4))
    ax_hist.plot(df["stock_price"].values[-100:], color="skyblue")
    ax_hist.set_title("Last 100 Data Points")
    ax_hist.grid(True)

    st.pyplot(fig_hist)

    # -------------------------------
    # PREDICTION BUTTON
    # -------------------------------
    if st.button("🚀 Predict Next 30 Days"):

        try:
            # ✅ Send last 10 rows (safe for VAR)
            input_data = df.values[-10:]

            response = requests.post(
                "http://127.0.0.1:8002/predict",
                json={"input": input_data.tolist()},
                timeout=10
            )

            # -------------------------------
            # HANDLE API FAILURE
            # -------------------------------
            if response.status_code != 200:
                st.error(f"API Error: {response.text}")
                st.stop()

            result = response.json()

            if "forecast" not in result:
                st.error(result)
                st.stop()

            # -------------------------------
            # FORECAST PROCESSING
            # -------------------------------
            preds = np.array(result["forecast"])

            # ✅ ALIGN WITH LAST VALUE (VERY IMPORTANT)
            offset = df["stock_price"].iloc[-1] - preds[0]
            preds = preds + offset

            # -------------------------------
            # FINAL PLOT (MATCH YOUR PROJECT)
            # -------------------------------
            st.subheader("📉 Forecast vs Historical")

            fig, ax = plt.subplots(figsize=(12, 5))

            hist = df["stock_price"].values[-100:]

            # Historical
            ax.plot(hist, label="Historical", color="black")

            # Forecast starts from end
            start = len(hist)

            ax.plot(
                range(start, start + len(preds)),
                preds,
                label="30-Day Forecast",
                color="red",
                linestyle="--",
                marker="o",
                markersize=4
            )

            ax.set_title("Apple Stock Price Forecast")
            ax.legend()
            ax.grid(True)

            st.pyplot(fig)

            # -------------------------------
            # DOWNLOAD OPTION
            # -------------------------------
            forecast_df = pd.DataFrame({
                "Day": list(range(1, 31)),
                "Forecasted_Price": preds
            })

            csv = forecast_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download Forecast CSV",
                data=csv,
                file_name="forecast_30_days.csv",
                mime="text/csv"
            )

            st.dataframe(forecast_df)

        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to API. Make sure FastAPI is running on port 8002")

        except requests.exceptions.Timeout:
            st.error("❌ API timeout. Try again.")

        except Exception as e:
            st.error(f"❌ Unexpected Error: {e}")

else:
    st.info("👆 Upload your dataset to start forecasting")
