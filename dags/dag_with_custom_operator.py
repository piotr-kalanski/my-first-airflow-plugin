from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from my_first_airflow_plugin.operators.my_custom_operator import MyCustomOperator
from datetime import datetime


with DAG('dag_with_custom_operator', start_date=datetime(2018, 8, 11)) as dag:
    (
        BashOperator(
            task_id='bash_hello',
            bash_command='echo "HELLO!"'
        )
        >> MyCustomOperator(
            task_id='task_with_custom_operator'
        )
    )
