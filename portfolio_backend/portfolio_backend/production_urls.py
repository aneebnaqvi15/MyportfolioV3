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
import sys
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(process)d %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

@csrf_exempt
def health_check(request):
    """Simplified health check that just verifies the application is responding"""
    logger.info(f"[HEALTH CHECK] Request received - Path: {request.path}, Method: {request.method}, Process: {os.getpid()}")
    
    try:
        return JsonResponse({
            "status": "healthy",
            "process_id": os.getpid(),
            "settings_module": os.environ.get('DJANGO_SETTINGS_MODULE', 'unknown')
        }, status=200)
    except Exception as e:
        logger.error(f"[HEALTH CHECK] Error in health check: {str(e)}")
        return JsonResponse({
            "status": "unhealthy",
            "error": str(e)
        }, status=500)

@csrf_exempt
def root(request):
    logger.info(f"[ROOT] Request received - Path: {request.path}, Method: {request.method}, Process: {os.getpid()}")
    return JsonResponse({
        "message": "Portfolio API",
        "version": "1.0",
        "status": "running"
    }, status=200)

# URL patterns
urlpatterns = [
    path('', root, name='root'),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Static file handling
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)