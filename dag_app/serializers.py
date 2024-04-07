from rest_framework import serializers
from .models import DAG, DAGRun


class DAGSerializer(serializers.ModelSerializer):
    run_count = serializers.SerializerMethodField()
    last_run = serializers.SerializerMethodField()

    class Meta:
        model = DAG
        fields = ['id', 'name', 'description', "default_args",
                  "paused", "start_date", "run_count", "last_run"]

    def get_run_count(self, instance):
        return instance.run_count()

    def get_last_run(self, instance):
        return instance.last_run()


class DAGRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = DAGRun
        fields = ['id', 'dag', 'run_date', 'status']
