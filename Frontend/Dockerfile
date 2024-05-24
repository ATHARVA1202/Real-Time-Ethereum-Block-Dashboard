FROM python:3.9-slim

WORKDIR /frontend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
EXPOSE 8502

CMD ["sh", "-c", "streamlit run block_data.py --server.port=8501 & streamlit run dashboard.py --server.port=8502"]
