# 📄 Apple Stock Forecasting System (Time Series + Cloud Deployment)

🚀 **Live Production Demo:** http://34.131.252.227:8501

🎯 Predicts future Apple stock prices using multivariate time series forecasting (VAR) with real-time API and interactive dashboard.

---

## 🎥 Live Demo (Quick Preview)

![Demo](screenshots/demo.gif)

---

## 📸 Dashboard Preview

### 📊 Historical Data

![Dashboard](screenshots/dashboard1.png)

### 📉 Forecast Visualization

![Forecast](screenshots/dashboard2.png)

---

## 🔥 Project Highlights

✔ Multivariate Time Series Forecasting using VAR
✔ Incorporates macroeconomic indicators (S&P 500, sentiment)
✔ Data preprocessing using differencing for stationarity
✔ Real-time prediction via FastAPI
✔ Interactive dashboard using Streamlit
✔ 30-day future forecasting capability
✔ End-to-end ML pipeline (data → model → deployment)
✔ Cloud deployment on GCP VM with static IP
✔ Production-style ML system design

---

## 🧠 Problem Statement

Stock prices are influenced by multiple external factors and are highly volatile.

👉 Traditional univariate models fail to capture interdependencies between variables.

👉 This project uses a **multivariate approach (VAR)** to model relationships between stock price, market index, and sentiment.

💼 **Impact:** Enables more realistic short-term forecasting and market trend analysis.

---

## 📊 Dataset

* Source: Synthetic + financial indicators dataset
* Size: ~100,000 rows
* Features:

  * stock_price
  * sp500_index
  * market_sentiment

### 🔧 Preprocessing

* Removed missing values
* Applied **first-order differencing** to ensure stationarity
* Selected relevant features for VAR modeling

---

## 🏗️ System Architecture

```
User
 ↓
Streamlit Dashboard
 ↓
FastAPI API
 ↓
Preprocessing (Differencing)
 ↓
VAR Model
 ↓
Forecast Output
```

---

## 🏗️ Architecture Details

* FastAPI handles real-time inference requests
* Streamlit provides interactive frontend visualization
* VAR model captures multivariate temporal dependencies
* Differencing ensures stable time series modeling
* Forecast results are reconstructed to original scale

---

## 🌐 Live Cloud Deployment

🚀 This project is deployed on Google Cloud Platform (GCP)

### 📊 Streamlit Dashboard
👉 http://34.131.252.227:8501

### ⚡ FastAPI Backend (API Docs)
👉 http://34.131.252.227:8002/docs

---

### 🧠 How it works
- Upload stock dataset
- Model processes time-series data using VAR
- Predicts next 30 days stock prices
- Visualizes forecast vs historical data

---

⚠️ Note:
- VM may be stopped to save cloud cost
- If link doesn’t work, please check later or contact me

---

## 🔌 API Example

```bash
curl -X POST "http://YOUR_VM_IP:8002/predict" \
-H "Content-Type: application/json" \
-d '{"input": [[500,4500,0.1],[501,4505,0.2],[502,4510,0.1],[503,4515,0.2],[504,4520,0.3]]}'
```

👉 Returns 30-day stock price forecast.

---

## 📈 Model Performance

The model was evaluated on a hold-out test set using standard regression metrics for time series forecasting.

### 📊 Evaluation Metrics

| Metric | Value | Interpretation |
|-------|------|----------------|
| **MAE (Mean Absolute Error)** | 4.39 | Average absolute prediction error |
| **RMSE (Root Mean Squared Error)** | 5.54 | Penalizes larger errors more heavily |
| **MSE (Mean Squared Error)** | 30.72 | Variance of prediction errors |
| **MAPE (Mean Absolute Percentage Error)** | **0.91%** | Very high accuracy (< 1%) |

---

### 🧠 Performance Insights

- The model achieves **<1% MAPE**, indicating highly accurate short-term forecasts  
- Low RMSE (~5.5) shows predictions remain close to actual price movements  
- Stable performance due to:
  - Multivariate modeling (VAR)
  - Stationarity via differencing
  - Proper feature selection

---

### 📌 Key Takeaway

👉 The model is **well-suited for short-term financial forecasting**  
👉 Provides **stable and realistic predictions**, avoiding extreme volatility  
👉 Production-ready for real-time inference use cases

---

## 🧠 Model Selection Rationale

* VAR captures relationships between multiple time-dependent variables
* Suitable for financial and economic data
* Lightweight and efficient compared to deep learning models
* Ideal for real-time API deployment

---

## ⚖️ Design Trade-offs

* VAR is fast and interpretable but assumes linear relationships
* Deep learning models (LSTM/Transformers) may improve accuracy but increase complexity
* Chosen approach balances **performance + speed + deployment simplicity**

---

## ⚠️ Limitations

* Assumes linear dependencies between variables
* Sensitive to non-stationary input data
* Forecast quality depends on input feature quality
* Free-tier cloud deployment may introduce latency

---

## ☁️ Deployment Details

* Platform: Google Cloud Platform (GCP VM)
* OS: Linux (Debian)
* Backend: FastAPI (Uvicorn)
* Frontend: Streamlit
* Networking: Static External IP

---

## ▶️ Run on Cloud VM

```bash
source env/bin/activate

uvicorn app_stock.app:app --host 0.0.0.0 --port 8002

streamlit run app_stock/ui.py --server.port 8501 --server.address 0.0.0.0
```

⚠️ If the app is not accessible, the VM instance may be stopped to save cost.

---

## 🧰 Tech Stack

* Python
* Pandas, NumPy
* Statsmodels (VAR)
* FastAPI
* Streamlit
* Matplotlib

---

## 📂 Project Structure

```
apple-stock-forecasting/
│
├── app_stock/
│   ├── app.py
│   └── ui.py
│
├── model/
│   ├── var_model.pkl
│   └── last_values.pkl
│
├── data/
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 💡 Key Learnings

* Built a real-world multivariate time series forecasting system
* Understood importance of preprocessing consistency (train vs inference)
* Integrated FastAPI with Streamlit for production pipeline
* Deployed ML system on cloud infrastructure
* Debugged real-world deployment and scaling issues

---

## 🎯 Use Cases

* Financial forecasting
* Market trend analysis
* Investment insights
* Economic modeling

---

## 🔮 Future Improvements

* Integrate LSTM / deep learning models
* Add real-time stock data (Yahoo Finance API)
* Include confidence intervals in forecasts
* Improve UI/UX for better visualization

---

## 👨‍💻 Author

**Kiran Kumar S R**

🎓 Data Science & AI Engineer
💼 Actively seeking Data Science / ML opportunities

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
