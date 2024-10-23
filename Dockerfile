FROM apache/airflow:2.10.2
COPY requirement.txt /requirement.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirement.txt
