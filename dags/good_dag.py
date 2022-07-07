from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from tasks import sql_test

default_args = {
    'owner': 'Joy',
    'depends_on_past': False,
    'start_date': datetime(2022, 7, 7),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}


dag = DAG(
    dag_id='sql_test_dag',
    description='sql_test',
    default_args=default_args,
    # schedule_interval='*/1 * * * *'
)


create = PythonOperator(
    task_id='create_table',
    python_callable=sql_test.create_table,
    provide_context=True,
    dag=dag
)

insert = PythonOperator(
    task_id='insert_row',
    python_callable=sql_test.insert_row,
    provide_context=True,
    dag=dag
)

update = PythonOperator(
    task_id='update',
    python_callable=sql_test.update_row,
    op_kwargs={
        '_id': insert.output,
        'enable': True
    },
    provide_context=True,
    dag=dag
)


create >> insert >> update
