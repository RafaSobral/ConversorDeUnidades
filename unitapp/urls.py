from django.urls import path
from . import views 

urlpatterns = [
    path('', views.tamanho, name='tamanho'),
    path('peso/', views.peso, name='peso'),
    path('temperatura/', views.temperatura, name='temperatura'),
]