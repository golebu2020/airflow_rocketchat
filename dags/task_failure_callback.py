from venv import logger
import requests
import json

def send_alert(context, dag):

    task_instance = context.get('task_instance')
    task_id = task_instance.task_id
    execution_date = context.get('execution_date')

    airflow_dag_logs = f""
    webhook_url = ''
    
    payload = {
    'text': f":warning: **{dag}**",
    'attachments': [
        {
            'color': '#d03ae8',
            'title': 'System Alert',
            'text': f"Task `{task_id}` failed on {dag} at {execution_date}. You can check logs here: [{airflow_dag_logs}]({airflow_dag_logs})",
            'fields': [
                {
                    'title': '**Action Required**',
                    'value': 'Immediate attention needed to resolve the issue.',
                }
            ]
        }
    ]
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(payload),
                             headers={'Content-Type': 'application/json'})
    except:
        logger.critical(f"Failed to send message for some reasons")
        
    if response.status_code != 200:
        logger.critical(f'Failed to send message. Status code {response.status_code}')
