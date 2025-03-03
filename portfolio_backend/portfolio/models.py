from django.db import models
from django.utils import timezone

# Create your models here.

class FirebaseModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Allow both URL and file upload for images
    image_url = models.URLField(max_length=500, blank=True, null=True)
    image_file = models.ImageField(upload_to='project_images/', blank=True, null=True)
    demo = models.URLField(max_length=500, blank=True, null=True, default='')
    github = models.URLField(max_length=500, blank=True, null=True)
    technologies = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def image(self):
        """Return either the uploaded image or the URL"""
        if self.image_file:
            return self.image_file.url
        return self.image_url or ''
