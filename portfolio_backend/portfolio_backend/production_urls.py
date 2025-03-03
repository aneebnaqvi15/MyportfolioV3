from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Simplified URL patterns for production
urlpatterns = [
    path('admin/', admin.site.urls),
    # Add a basic health check endpoint
    path('health/', lambda request: HttpResponse("OK")),
]

# Add static and media URL patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 