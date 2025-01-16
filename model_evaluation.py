import os
import pandas as pd
from sklearn.metrics import silhouette_score

import mlflow

DATA_PATH = "/opt/airflow/data"
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "file:/opt/airflow/mlruns")

def evaluate_model(**context):
    """
    5) Evaluate the model using silhouette score, log metric to MLflow.
    """
    input_file = f"{DATA_PATH}/random_data_preprocessed.csv"
    df = pd.read_csv(input_file)

    cluster_labels = context['ti'].xcom_pull(key="cluster_labels", task_ids="train_model")
    if cluster_labels is None:
        print("[evaluate_model] No cluster labels found in XCom; skipping.")
        return

    score = silhouette_score(df, cluster_labels)
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    with mlflow.start_run(run_name="unsupervised_evaluation"):
        mlflow.log_metric("silhouette_score", score)

    print(f"[evaluate_model] Silhouette Score: {score}")


def register_model(**context):
    """
    6) (Optional) Register the model in MLflow’s Model Registry.
       Requires a backend store that supports a registry.
    """
    print("[register_model] Model registration is optional with local file-based MLflow.")
