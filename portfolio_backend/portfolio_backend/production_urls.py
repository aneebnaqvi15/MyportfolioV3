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
from django.views.generic import TemplateView
from django.shortcuts import render

@csrf_exempt
def root(request):
    return JsonResponse({
        "message": "Portfolio API",
        "version": "1.0",
        "status": "running"
    })

def serve_portfolio(request):
    return render(request, '../../pf/html/index.html')

# URL patterns
urlpatterns = [
    # Serve portfolio as main page
    path('', serve_portfolio, name='portfolio'),
    
    # API endpoints
    path('api/', root, name='api-root'),
    path('api/admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Static file handling
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add static files serving for production
urlpatterns += static('/', document_root='pf')