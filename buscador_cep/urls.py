
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultado.html/', views.resultado, name='resultado'),
    path('api/cep/<cep>',  views.consulta_cep, name='API'),
]
