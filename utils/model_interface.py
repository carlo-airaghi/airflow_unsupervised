import os
import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn

DATA_PATH = "/opt/airflow/data"
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "file:/opt/airflow/mlruns")

def inference(**context):
    """
    7) (Optional) Perform inference on new data or a hold-out set using the trained model.
    """
    # Example new data
    new_data = np.random.rand(5, 5)  # 5 new samples
    df_new = pd.DataFrame(new_data, columns=[f"feature_{i}" for i in range(5)])

    # In a real scenario, you would fetch the run_id from XCom or MLflow,
    # then load the trained model from MLflow:
    #
    # mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    # run_id = <some_run_id>
    # model_uri = f"runs:/{run_id}/models"
    # loaded_model = mlflow.sklearn.load_model(model_uri)
    #
    # cluster_assignments = loaded_model.predict(df_new)
    # print("[inference] New data cluster assignments:", cluster_assignments)

    print("[inference] This is a demo. Load and apply the model as per your MLflow setup.")
