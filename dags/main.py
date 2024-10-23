from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime
from task_failure_callback import send_alert

"""
DAG: airflow_failure_test

This DAG is a simple script to demonstrate failure handling and sending of rocektchat alerts in Airflow. 
It's not a functional component of the code base
"""

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),  
}

with DAG(
    'acs_dev',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(minutes=3),  # Run every 3 minutes
    start_date=datetime(2024, 10, 15),
    catchup=False,
) as dag:

    def test_dag_task():
        print("Hello, dag task!")
        raise Exception('The task has failed intentionally')

    t1 = PythonOperator(
        task_id='test_dag_task',
        python_callable=test_dag_task,
        on_failure_callback=lambda context: send_alert(context, "acs_dev")
    )

