from datetime import datetime
from typing import Union

from django.db import models


class DAG(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule_interval = models.CharField(max_length=50, help_text="E.g @daily")
    # default_args = {
    #     "owner": "i-wizard",
    #     "retries": 5,
    #     "retry_delay": 300  # represented as an int in seconds
    # }
    default_args = models.JSONField(default=dict)
    start_date = models.DateTimeField()
    paused = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def last_run(self) -> Union[datetime, None]:
        dag_run = self.runs.all().order_by("-run_date").only("run_date").first()
        if dag_run:
            return dag_run.run_date
        return None

    def run_count(self) -> int:
        return self.runs.count()


class DAGRun(models.Model):
    STATUS_CHOICES = (
        ("QUEUED", "QUEUED"),
        ("SUCCESS", "SUCCESS"),
        ("FAILED", "FAILED"),
        ("RUNNING", "RUNNING"),
    )
    dag = models.ForeignKey(DAG, on_delete=models.CASCADE, related_name='runs')
    run_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.dag.name} - {self.run_date} - {self.status}"
