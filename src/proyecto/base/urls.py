from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Lista_Bancos, inicio

urlpatterns = [
    path('GraficaEChart/', Lista_Bancos.as_view(), name='bancos'),
    path('generar_bancos/', views.generar_bancos, name='generar_bancos'),
    path('', views.inicio, name='inicio'),
    path('api/', include('api.urls'))
]
