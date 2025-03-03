from rest_framework import serializers
from .models import Project, Skill, Certification

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image_url', 'github', 'technologies', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # Create new project
        project = Project.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        # Update existing project
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.github = validated_data.get('github', instance.github)
        instance.technologies = validated_data.get('technologies', instance.technologies)
        instance.save()
        return instance

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__' 