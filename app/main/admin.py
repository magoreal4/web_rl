from django.contrib import admin
from .models import Banner, Logos, Servicios


admin.site.register(Banner)
admin.site.register(Servicios)
admin.site.register(Logos)
admin.site.site_header = "Red Line"
admin.site.site_title = "Panel de Gestion"