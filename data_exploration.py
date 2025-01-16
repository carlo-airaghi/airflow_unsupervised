import os
import pandas as pd
from ydata_profiling import ProfileReport

DATA_PATH = "/opt/airflow/data"
PROFILE_REPORTS_PATH = "/opt/airflow/data/profiles"

def data_exploration(**context):
    """
    2) Explore data using ydata-profiling, generate an HTML report.
    """
    csv_path = f"{DATA_PATH}/random_data.csv"
    df = pd.read_csv(csv_path)

    os.makedirs(PROFILE_REPORTS_PATH, exist_ok=True)
    profile = ProfileReport(df, title="Data Exploration Report", explorative=True)
    
    report_path = f"{PROFILE_REPORTS_PATH}/random_data_profile.html"
    profile.to_file(report_path)
    print(f"[data_exploration] Profiling report generated at: {report_path}")
