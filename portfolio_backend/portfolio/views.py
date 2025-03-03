from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FirebaseModel
from rest_framework import viewsets
from .serializers import FirebaseModelSerializer

# Create your views here.

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

class FirebaseModelViewSet(viewsets.ModelViewSet):
    queryset = FirebaseModel.objects.all()
    serializer_class = FirebaseModelSerializer
