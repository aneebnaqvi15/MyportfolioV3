from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, require_http_methods
import json
from .models import Project, FirebaseModel, Skill, Certification, Certificate
import logging
from django.urls import get_resolver
from firebase_admin import firestore
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProjectSerializer, SkillSerializer, CertificationSerializer
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings

logger = logging.getLogger(__name__)

db = firestore.client()

class Project(Project):
    collection_name = 'projects'

@csrf_exempt
def home(request):
    return JsonResponse({"message": "Welcome to Portfolio API"})

@csrf_exempt
def project_list(request):
    if request.method == 'GET':
        projects = Project.get_all()
        # Update GitHub URLs
        for project in projects:
            project['github'] = settings.GITHUB_REPO_URL
        return JsonResponse({"projects": projects})
    elif request.method == 'POST':
        data = json.loads(request.body)
        data['github'] = settings.GITHUB_REPO_URL  # Set correct GitHub URL
        project = Project.create(data)
        return JsonResponse({"message": "Project created", "project": project})

@csrf_exempt
def project_detail(request, project_id):
    if request.method == 'GET':
        project = Project.get_by_id(project_id)
        if project:
            return JsonResponse({"project": project})
        return JsonResponse({"error": "Project not found"}, status=404)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        project = Project.update(project_id, data)
        return JsonResponse({"message": "Project updated", "project": project})
    elif request.method == 'DELETE':
        Project.delete(project_id)
        return JsonResponse({"message": "Project deleted"})

@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Add your contact form submission logic here
        return JsonResponse({"message": "Message sent successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_projects(request):
    """Fetch projects from Firebase"""
    try:
        # Get projects collection from Firebase
        projects_ref = db.collection('projects')
        projects = projects_ref.get()
        
        # Convert to list of dictionaries
        projects_list = []
        for project in projects:
            project_data = project.to_dict()
            project_data['id'] = project.id
            projects_list.append(project_data)
        
        return JsonResponse(projects_list, safe=False)
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return JsonResponse({'error': str(e)}, status=500)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = FirebaseModel.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request, *args, **kwargs):
        try:
            projects = self.get_queryset()
            logger.info(f"Found {projects.count()} projects")
            
            serializer = self.get_serializer(projects, many=True)
            data = serializer.data
            
            # Update GitHub URLs in response
            for project in data:
                project['github'] = settings.GITHUB_REPO_URL
            
            return Response({
                'status': 'success',
                'data': data
            })
        except Exception as e:
            logger.error(f"Error in list view: {str(e)}")
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.dict() if hasattr(request.data, 'dict') else request.data
            logger.info(f"Received project data: {data}")
            
            # Set correct GitHub URL
            data['github'] = settings.GITHUB_REPO_URL
            
            if 'image_file' in request.FILES:
                image_file = request.FILES['image_file']
                file_name = default_storage.save(f'projects/{image_file.name}', image_file)
                data['image_url'] = f'/media/projects/{image_file.name}'
                logger.info(f"Saved image at: {data['image_url']}")

            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                project = serializer.save()
                logger.info(f"Created project: {project.title}")
                return Response({
                    'status': 'success',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Serializer errors: {serializer.errors}")
                return Response({
                    'status': 'error',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error in create view: {str(e)}")
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def debug_view(request):
    """Debug view to show all available URLs"""
    patterns = []
    for pattern in get_resolver().url_patterns:
        patterns.append(str(pattern.pattern))
    return JsonResponse({
        'patterns': patterns,
        'current_url': request.build_absolute_uri(),
    })

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('category', '-percentage')
    serializer_class = SkillSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all().order_by('-date_earned')
    serializer_class = CertificationSerializer

@ensure_csrf_cookie  # This ensures the CSRF cookie is set
def get_csrf_token(request):
    return JsonResponse({'status': 'CSRF cookie set'})

@require_http_methods(["POST"])
def add_skill(request):
    try:
        data = json.loads(request.body)
        skill = Skill.objects.create(
            name=data['name'],
            category=data['category'],
            icon_url=data['icon_url']
        )
        return JsonResponse({
            'status': 'success',
            'skill': {
                'id': skill.id,
                'name': skill.name,
                'category': skill.category,
                'icon_url': skill.icon_url
            }
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def skill_list(request):
    if request.method == "GET":
        skills = Skill.objects.all()
        data = list(skills.values())
        return JsonResponse(data, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            skill = Skill.objects.create(
                name=data['name'],
                category=data['category'],
                icon_url=data['icon_url']
            )
            return JsonResponse({
                'status': 'success',
                'skill': {
                    'id': skill.id,
                    'name': skill.name,
                    'category': skill.category,
                    'icon_url': skill.icon_url
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def certificate_list(request):
    if request.method == "GET":
        certificates = Certificate.objects.all()
        data = list(certificates.values())
        return JsonResponse(data, safe=False)
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            certificate = Certificate.objects.create(
                title=data['title'],
                issuer=data['issuer'],
                issue_date=data['issue_date'],
                credential_url=data['credential_url'],
                image_url=data['image_url']
            )
            return JsonResponse({
                'status': 'success',
                'certificate': {
                    'id': certificate.id,
                    'title': certificate.title,
                    'issuer': certificate.issuer,
                    'issue_date': certificate.issue_date,
                    'credential_url': certificate.credential_url,
                    'image_url': certificate.image_url
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)