from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
   'owner': 'Airflow',
   'depends_on_past': False,
   'email': 'john.mattern@noaa.gov',
   'start_date': datetime(2020, 7, 2),
   'email_on_failure': True,
}


dag = DAG('games', default_args=default_args, schedule_interval=None)
#dag = DAG('games', default_args=default_args, schedule_interval="* * * *")
#dag = DAG('games', default_args=default_args, schedule_interval=timedelta(days=1))


t1 = BashOperator(
   task_id='sklearn_pipeline',
   bash_command='docker run sklearn_pipeline',
   dag=dag)
