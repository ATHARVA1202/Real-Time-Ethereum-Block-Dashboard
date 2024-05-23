# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /frontend

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app files into the container
COPY . .

# Expose the Streamlit ports
EXPOSE 8501
EXPOSE 8502

# Run Streamlit apps
CMD ["sh", "-c", "streamlit run block_data.py --server.port=8501 & streamlit run dashboard.py --server.port=8502"]
