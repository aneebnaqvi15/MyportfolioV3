from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FirebaseModel
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FirebaseModelSerializer
from django.conf import settings

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = FirebaseModel.objects.all().order_by('-created_at')
    serializer_class = FirebaseModelSerializer

    def list(self, request, *args, **kwargs):
        try:
            projects = self.get_queryset()
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
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.dict() if hasattr(request.data, 'dict') else request.data
            
            # Set correct GitHub URL
            data['github'] = settings.GITHUB_REPO_URL
            
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                project = serializer.save()
                return Response({
                    'status': 'success',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'error',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def debug_view(request):
    """Debug view to show all available URLs"""
    return JsonResponse({
        'message': 'Debug endpoint is working'
    })

class Project(FirebaseModel):
    collection_name = 'projects'

@csrf_exempt
def home(request):
    return JsonResponse({"message": "Welcome to Portfolio API"})

@csrf_exempt
def project_list(request):
    if request.method == 'GET':
        projects = Project.get_all()
        return JsonResponse({"projects": projects})
    elif request.method == 'POST':
        data = json.loads(request.body)
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
