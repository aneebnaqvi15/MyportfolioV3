from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def health_check(request):
    try:
        # Try to make a simple database query to verify DB connection
        from django.contrib.auth.models import User
        User.objects.first()
        
        # Check if SECRET_KEY is set
        if not settings.SECRET_KEY:
            raise Exception("SECRET_KEY is not set")
            
        return JsonResponse({
            "status": "healthy",
            "database": "connected",
            "secret_key": "configured"
        }, status=200)
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return JsonResponse({
            "status": "unhealthy",
            "error": str(e),
            "type": type(e).__name__
        }, status=500)

@csrf_exempt
def root(request):
    logger.info(f"Root path accessed. Path: {request.path}, Method: {request.method}")
    return JsonResponse({
        "message": "Portfolio API",
        "version": "1.0",
        "status": "running",
        "endpoints": {
            "admin": "/admin/",
            "health": "/health/",
            "api_token": "/api/token/",
            "api_token_refresh": "/api/token/refresh/",
            "api_token_verify": "/api/token/verify/"
        }
    }, status=200)

# Simplified URL patterns for production
urlpatterns = [
    # Root path handler
    path('', root, name='root'),
    path('health/', health_check, name='health_check'),
    
    # Admin and authentication
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Add static and media URL patterns if in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add a catch-all pattern for debugging
if settings.DEBUG:
    def debug_404(request):
        logger.warning(f"404 for path: {request.path}, Method: {request.method}")
        return JsonResponse({
            "error": "Not Found",
            "path": request.path,
            "method": request.method,
            "available_paths": [str(pattern.pattern) for pattern in urlpatterns]
        }, status=404)
    
    urlpatterns.append(path('<path:path>', debug_404)) 