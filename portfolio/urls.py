from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, debug_urls, FirebaseModelViewSet, SkillViewSet, CertificationViewSet, add_skill, get_csrf_token, skill_list, certificate_list

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'firebase', FirebaseModelViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('debug/', debug_urls, name='debug-urls'),
    path('api/get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('api/skills/', add_skill, name='add_skill'),
    path('api/firebase/skills/', skill_list, name='skill_list'),
    path('api/firebase/certificates/', certificate_list, name='certificate_list'),
] 