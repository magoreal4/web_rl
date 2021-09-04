from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Banner, Logos, Servicios


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        banner = Banner.objects.all()
        servicios = Servicios.objects.all()
        logos = Logos.objects.all()
        print(banner)
        return {'banner': banner, 'servicios': servicios, 'logos': logos}


class ServiciosPrestados(ListView):
    template_name = "servicios.html"
    model = Servicios
    context_object_name = "servicios"