FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app_stock ./app_stock
COPY model ./model

EXPOSE 8002

CMD ["uvicorn", "app_stock.app:app", "--host", "0.0.0.0", "--port", "8002"]