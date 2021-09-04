from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('servicios/', views.ServiciosPrestados.as_view(), name='Servicios')
]