import pytest
from airflow.models import DagBag


def test_dagbag_import_errors():
    """Тест проверяет, что Airflow может успешно распарсить все DAG-файлы."""
    # Указываем папку, где лежат твои DAG
    dag_bag = DagBag(dag_folder="dags", include_examples=False)

    # Собираем ошибки импорта
    import_errors = dag_bag.import_errors

    # Если ошибок нет, длина словаря import_errors будет равна 0
    assert len(import_errors) == 0, f"Airflow обнаружил ошибки при импорте DAG: {import_errors}"