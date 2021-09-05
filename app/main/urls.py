from django.urls import path
from main import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('servicios/', views.ServiciosPrestados.as_view(), name='Servicios'),
    path('prueba/', views.Prueba.as_view(), name='Prueba')
]