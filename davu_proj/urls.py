"""davu_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls


schema_view = yasg_get_schema_view(
   openapi.Info(
      title="Davu Airflow DAG Management API",
      default_version='v1',
      description="Davu API to manage DAGs and DAG runs in Apache Airflow",
      contact=openapi.Contact(email="njoagwuanidavid@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('dag_app.urls')),
    path('docs/', include_docs_urls(title='Airflow DAG Management API')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

