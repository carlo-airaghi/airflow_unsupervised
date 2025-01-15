# Start from a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /mlflow

# Install MLflow and required dependencies
RUN pip install --no-cache-dir mlflow

# Expose the default MLflow server port
EXPOSE 5000

# Define the command to start the MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "file:/mlruns"]
