from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from decouple import config


urlpatterns = [
    path("", include("core.urls")),
    path("", include("store.urls")),
    path("compte/", include("authentication.urls")),
    path(config('ADMIN_PANEL'), admin.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin site configuration
admin.site.site_header = "SERVICES KENEYATON SARL"
admin.site.site_title = "Portail d'administration Services Keneyaton Sarl"
admin.site.index_title = "Bienvenue"