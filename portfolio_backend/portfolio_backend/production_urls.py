from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    try:
        # Try to make a simple database query to verify DB connection
        from django.contrib.auth.models import User
        User.objects.first()
        return JsonResponse({"status": "healthy"}, status=200)
    except Exception as e:
        return JsonResponse({"status": "unhealthy", "error": str(e)}, status=500)

@csrf_exempt
def root(request):
    return JsonResponse({"message": "Portfolio API"}, status=200)

# Simplified URL patterns for production
urlpatterns = [
    path('', root, name='root'),
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
]

# Add static and media URL patterns if in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 