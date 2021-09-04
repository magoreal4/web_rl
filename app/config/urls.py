from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic.base import RedirectView
# from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact/', include('fcontact.urls')),
    # path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

