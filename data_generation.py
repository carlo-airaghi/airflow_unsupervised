import os
import numpy as np
import pandas as pd

DATA_PATH = "/opt/airflow/data"

def generate_data(**context):
    """
    1) Generate random numeric data and save to CSV.
    """
    os.makedirs(DATA_PATH, exist_ok=True)
    
    data = np.random.rand(1000, 5)  # 1000 samples, 5 features
    df = pd.DataFrame(data, columns=[f"feature_{i}" for i in range(5)])
    
    csv_path = f"{DATA_PATH}/random_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"[generate_data] Created random_data.csv with shape={df.shape}")
