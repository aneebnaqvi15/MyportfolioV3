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
from django.shortcuts import render, redirect
import os

@csrf_exempt
def root(request):
    return JsonResponse({
        "message": "Portfolio API",
        "version": "1.0",
        "status": "running",
        "github": settings.GITHUB_REPO_URL
    })

def serve_static_file(request, path):
    """Serve static files or redirect to GitHub Pages in production"""
    if settings.DEBUG:
        file_path = os.path.join(settings.PROJECT_ROOT, 'pf', path)
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        return HttpResponse(status=404)
    else:
        # In production, redirect to GitHub Pages
        return redirect(f"{settings.GITHUB_PAGES_URL}/{path}")

def serve_portfolio(request):
    """Serve portfolio or redirect to GitHub Pages in production"""
    if settings.DEBUG:
        return render(request, 'index.html')
    else:
        # In production, redirect to GitHub Pages
        return redirect(settings.GITHUB_PAGES_URL)

# URL patterns
urlpatterns = [
    # API endpoints under /api/
    path('api/', root, name='api-root'),
    path('api/admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Serve portfolio files
    re_path(r'^(?P<path>js/.*|css/.*|images/.*|data/.*|html/.*)$', serve_static_file),
    
    # Serve index.html for the root path
    path('', serve_portfolio, name='portfolio'),
]

# Add static and media file handling
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)