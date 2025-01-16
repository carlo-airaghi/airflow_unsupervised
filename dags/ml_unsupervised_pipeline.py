"""
Airflow DAG for an extended unsupervised ML pipeline with separate utils modules.
"""

import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Import our functions from utils
from utils.data_generation import generate_data
from utils.data_exploration import data_exploration
from utils.data_preprocessing import preprocess_data
from utils.model_training import train_model
from utils.model_evaluation import evaluate_model, register_model
from utils.model_inference import inference
from utils.notifications import notify_slack

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="ml_unsupervised_pipeline_extended",
    default_args=default_args,
    description="Extended unsupervised ML pipeline with data exploration, training, evaluation",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1,
) as dag:

    task_generate_data = PythonOperator(
        task_id="generate_data",
        python_callable=generate_data,
    )

    task_data_exploration = PythonOperator(
        task_id="data_exploration",
        python_callable=data_exploration,
    )

    task_preprocess_data = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data,
    )

    task_train_model = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )

    task_evaluate_model = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model,
    )

    task_register_model = PythonOperator(
        task_id="register_model",
        python_callable=register_model,
    )

    task_inference = PythonOperator(
        task_id="inference",
        python_callable=inference,
    )

    task_notify_slack = PythonOperator(
        task_id="notify_slack",
        python_callable=notify_slack,
        trigger_rule="all_done",  # Run notification regardless of success/failure
    )

    # Define the DAG order:
    # 1) Generate -> 2) Explore -> 3) Preprocess -> 4) Train -> 5) Evaluate
    # 6) Register -> 7) Inference -> 8) Notify
    task_generate_data >> task_data_exploration >> task_preprocess_data >> task_train_model >> task_evaluate_model
    task_evaluate_model >> task_register_model >> task_inference >> task_notify_slack
