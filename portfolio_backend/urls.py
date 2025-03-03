from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),  # Include portfolio URLs under /api/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Print URL patterns for debugging
print("\nRegistered URL patterns:")
for pattern in urlpatterns:
    print(f"  {pattern}")