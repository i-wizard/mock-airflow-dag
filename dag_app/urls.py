from django.urls import path, include
from rest_framework import routers
from .views import DAGViewSet, DAGRunViewSet

router = routers.DefaultRouter()
router.register(r'dags', DAGViewSet)
router.register(r'dagruns', DAGRunViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
