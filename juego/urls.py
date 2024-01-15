from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juego/', views.juego, name='juego'),
    path('registro/', views.registro, name='registro'),


]