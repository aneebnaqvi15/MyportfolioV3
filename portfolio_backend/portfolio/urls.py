from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, debug_view

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('debug/', debug_view, name='debug'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)