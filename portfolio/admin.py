from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Project, Education, Skill, Contact, Certification, Certificate

class FirebaseModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.firebase_list_view), name='firebase_list'),
        ]
        return custom_urls + urls

    def firebase_list_view(self, request):
        model = self.model
        objects = model.get_all()
        context = {
            'objects': objects,
            'title': f'{model.collection_name.title()} List',
        }
        return render(request, 'admin/firebase_list.html', context)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at')
    search_fields = ('title', 'description', 'technologies')

@admin.register(Education)
class EducationAdmin(FirebaseModelAdmin):
    list_display = ('institution', 'degree', 'duration')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_earned', 'created_at')
    list_filter = ('issuer', 'date_earned')
    search_fields = ('title', 'issuer')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date')
    list_filter = ('issuer', 'issue_date')
    search_fields = ('title', 'issuer') 