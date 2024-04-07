from rest_framework import viewsets
from .models import DAG, DAGRun
from .serializers import DAGSerializer, DAGRunSerializer


class DAGViewSet(viewsets.ModelViewSet):
    queryset = DAG.objects.all()
    serializer_class = DAGSerializer


class DAGRunViewSet(viewsets.ModelViewSet):
    queryset = DAGRun.objects.all()
    serializer_class = DAGRunSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.dag.paused = False  # Running a dag should automaticall unpause it
        instance.dag.save(update_fields=['paused'])
