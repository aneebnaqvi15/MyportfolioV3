from django.db import migrations

def add_initial_projects(apps, schema_editor):
    FirebaseModel = apps.get_model('portfolio', 'FirebaseModel')
    
    # Your existing projects data
    initial_projects = [
        {
            'title': 'Portfolio Website',
            'description': 'A modern portfolio website built with HTML, CSS, and JavaScript.',
            'image_url': '../images/project1.jpg',  # Update with your actual image paths
            'github': 'https://github.com/aneebnaqvi15/portfolio',
            'technologies': 'HTML, CSS, JavaScript, GSAP'
        },
        # Add your other existing projects here
        {
            'title': 'Project 2',
            'description': 'Your project 2 description',
            'image_url': '../images/project2.jpg',
            'github': 'https://github.com/yourusername/project2',
            'technologies': 'React, Node.js, MongoDB'
        },
        # Add more projects as needed
    ]
    
    for project in initial_projects:
        FirebaseModel.objects.create(**project)

def remove_initial_projects(apps, schema_editor):
    FirebaseModel = apps.get_model('portfolio', 'FirebaseModel')
    FirebaseModel.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0006_remove_firebasemodel_image_firebasemodel_image_file_and_more'),
    ]

    operations = [
        migrations.RunPython(add_initial_projects, remove_initial_projects),
    ] 