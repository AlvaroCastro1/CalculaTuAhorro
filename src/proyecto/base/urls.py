from django.urls import path
from . import views
from .views import Lista_Bancos

urlpatterns = [
    path('', Lista_Bancos.as_view(), name='bancos'),
    path('generar_bancos/', views.generar_bancos, name='generar_bancos'),
    ]