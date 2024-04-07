from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import DAG, DAGRun
from .serializers import DAGSerializer, DAGRunSerializer


def create_dag_payload() -> dict:
    return {
        "name": "Test Dag",
        "description": "Test description",
        "start_date": datetime.now(),
        "schedule_interval": "@daily",
        "default_args": {
            "owner": "i-wizard",
            "retries": 5,
            "retry_delay": 300
        }
    }


@pytest.mark.django_db
def test_create_dag():
    client = APIClient()
    url = reverse('dag-list')
    data = create_dag_payload()
    assert DAG.objects.count() == 0
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert DAG.objects.count() == 1
    dag = DAG.objects.get()
    assert dag.name == data['name']
    assert dag.paused is True


@pytest.mark.django_db
def test_get_dags():
    DAG.objects.create(**create_dag_payload())
    client = APIClient()
    url = reverse('dag-list')
    response = client.get(url)
    dags = DAG.objects.all()
    serializer = DAGSerializer(dags, many=True)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_dag_run():
    dag = DAG.objects.create(
        **create_dag_payload())
    client = APIClient()
    url = reverse('dagrun-list')
    data = {'dag': dag.id, 'status': 'QUEUED'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert dag.run_count() == 1
    dag_run = DAGRun.objects.get()
    assert dag_run.status == data['status']

    # Ensure the related dag is now unpaused after running
    dag.refresh_from_db()
    assert dag.paused is False


@pytest.mark.django_db
def test_get_dag_runs():
    dag = DAG.objects.create(**create_dag_payload())
    DAGRun.objects.create(dag=dag, status='SUCCESS')
    client = APIClient()
    url = reverse('dagrun-list')
    response = client.get(url)
    dag_runs = dag.runs.all()
    serializer = DAGRunSerializer(dag_runs, many=True)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK
