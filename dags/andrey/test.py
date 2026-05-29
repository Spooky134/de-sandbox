from datetime import datetime
from airflow.decorators import dag, task

@dag(
    dag_id="airflow3_sandbox_test",
    schedule=None,         # Только ручной запуск из UI
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["sandbox"],
)
def sandbox_test_dag():

    @task
    def extract_data():
        return {"project": "Sandbox", "version": "3.2.1", "status": "active"}

    @task
    def transform_data(data: dict):
        # Преобразуем данные в строку
        info_str = f"Проект {data['project']} на Airflow {data['version']} работает!"
        return info_str.upper()

    @task
    def load_data(result: str):
        # Выводим финальный результат в логи
        print("=" * 40)
        print(result)
        print("=" * 40)

    # Выстраиваем цепочку зависимостей (данные передаются из таски в таску)
    raw_data = extract_data()
    transformed_msg = transform_data(raw_data)
    load_data(transformed_msg)
    load_data(transformed_msg)

# Инициализируем DAG
sandbox_test_dag()