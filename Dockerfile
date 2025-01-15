# Start from the Airflow base image
FROM apache/airflow:2.9.3

# Set the working directory
WORKDIR /opt/airflow

# Copy the requirements.txt file into the image
COPY requirements.txt /opt/airflow/requirements.txt

# Install the packages listed in requirements.txt
RUN pip install -r /opt/airflow/requirements.txt

