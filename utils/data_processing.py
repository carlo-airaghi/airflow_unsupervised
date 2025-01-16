import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

DATA_PATH = "/opt/airflow/data"

def preprocess_data(**context):
    """
    3) Preprocess data: scaling, transformations, etc.
       Save the transformed data to random_data_preprocessed.csv
    """
    input_file = f"{DATA_PATH}/random_data.csv"
    output_file = f"{DATA_PATH}/random_data_preprocessed.csv"
    
    df = pd.read_csv(input_file)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    
    df_scaled = pd.DataFrame(scaled_data, columns=df.columns)
    df_scaled.to_csv(output_file, index=False)
    print(f"[preprocess_data] Preprocessed data saved to {output_file} (shape={df_scaled.shape})")
