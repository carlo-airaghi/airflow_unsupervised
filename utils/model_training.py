import os
import pandas as pd
from sklearn.cluster import KMeans

import mlflow
import mlflow.sklearn

DATA_PATH = "/opt/airflow/data"
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "file:/opt/airflow/mlruns")

def train_model(**context):
    """
    4) Train an unsupervised model (K-Means) and log params/models to MLflow.
    """
    input_file = f"{DATA_PATH}/random_data_preprocessed.csv"
    df = pd.read_csv(input_file)

    n_clusters = 3
    model = KMeans(n_clusters=n_clusters, random_state=42)

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    with mlflow.start_run(run_name="unsupervised_training"):
        mlflow.log_param("n_clusters", n_clusters)
        model.fit(df)

        # Log the model
        mlflow.sklearn.log_model(model, artifact_path="models")

        # Store cluster labels in XCom
        context['ti'].xcom_push(key="cluster_labels", value=model.labels_.tolist())

    print("[train_model] Model trained and logged to MLflow.")
