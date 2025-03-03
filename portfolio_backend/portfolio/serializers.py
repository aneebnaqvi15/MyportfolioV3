from rest_framework import serializers
from .models import FirebaseModel

class FirebaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseModel
        fields = ['id', 'title', 'description', 'image_url', 'image_file', 
                 'github', 'technologies', 'created_at', 'updated_at', 'image'] 