from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.views.generic import TemplateView
from django.shortcuts import render
import os
import mimetypes

def serve_static_file(request, path):
    """Serve static files directly"""
    file_path = os.path.join(settings.PROJECT_ROOT, 'pf', path)
    if os.path.exists(file_path):
        content_type, _ = mimetypes.guess_type(file_path)
        response = FileResponse(open(file_path, 'rb'))
        if content_type:
            response['Content-Type'] = content_type
        return response
    return HttpResponse(status=404)

def serve_portfolio(request):
    """Serve the portfolio's index.html file"""
    file_path = os.path.join(settings.PROJECT_ROOT, 'pf', 'html', 'index.html')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='text/html')
    return HttpResponse(status=404)

# API endpoints
@csrf_exempt
def api_root(request):
    return JsonResponse({
        "message": "Portfolio API",
        "version": "1.0",
        "status": "running",
        "github": settings.GITHUB_REPO_URL
    })

# URL patterns
urlpatterns = [
    # Serve portfolio files
    re_path(r'^(?P<path>js/.*|css/.*|images/.*|data/.*)$', serve_static_file),
    
    # API endpoints under /api/
    path('api/', api_root, name='api-root'),
    path('api/admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Serve index.html for all other paths
    re_path(r'^.*$', serve_portfolio, name='portfolio'),
]

# Add static and media file handling for development
if settings.DEBUG:
    urlpatterns = [
        path('', serve_portfolio, name='portfolio'),
    ] + urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)