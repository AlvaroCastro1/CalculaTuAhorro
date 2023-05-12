from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_bancos, name='bancos'),
    path('generar_bancos/', views.generar_bancos, name='generar_bancos'),
    ]