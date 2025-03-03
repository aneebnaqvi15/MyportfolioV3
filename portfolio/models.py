from django.db import models
from firebase_admin import firestore

db = firestore.client()

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    image_file = models.ImageField(upload_to='projects/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def image(self):
        if self.image_file:
            return self.image_file.url
        return self.image_url or ''

class FirebaseModel(models.Model):
    # Define your model fields here
    # For example:
    title = models.CharField(max_length=200)
    description = models.TextField()
    # ... add other fields as needed

    def __str__(self):
        return self.title  # or any other field you want to use as string representation

class Education(FirebaseModel):
    collection_name = 'education'

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    icon_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Certification(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=100)
    icon_url = models.URLField()
    learning_points = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    credential_url = models.URLField(blank=True, null=True)
    view_certificate_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-end_date']

    def get_learning_points(self):
        return self.learning_points.split('\n')

class Contact(FirebaseModel):
    collection_name = 'contacts'

    def __str__(self):
        return f"Message from {self.name}"

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    icon_url = models.URLField()
    details = models.JSONField()  # Store list of details
    issue_date = models.CharField(max_length=50)  # e.g., "Dec 2023"
    credential_url = models.URLField()
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.title} - {self.issuer}" 