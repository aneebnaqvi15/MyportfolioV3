from django.contrib import admin
from django.urls import path, include
from portfolio.views import ProjectViewSet, debug_view, get_projects
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'firebase', ProjectViewSet)

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/debug/', debug_view, name='debug'),  # Add debug view under /api/
    path('api/projects/', get_projects, name='get-projects'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Print URL patterns for debugging
print("\nRegistered URL patterns:")
for pattern in urlpatterns:
    print(f"  {pattern}")