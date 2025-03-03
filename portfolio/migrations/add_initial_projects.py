from django.db import migrations

def add_initial_projects(apps, schema_editor):
    FirebaseModel = apps.get_model('portfolio', 'FirebaseModel')
    
    projects = [
        {
            'title': 'Event Registration System',
            'description': 'A comprehensive event registration platform built with modern web technologies.',
            'image_url': './images/event-registration.jpg',
            'github': 'https://github.com/aneebnaqvi15/event-registration-system',
            'technologies': 'HTML, CSS, JavaScript, Django'
        },
        {
            'title': 'Job Portal',
            'description': 'An online job portal connecting employers with potential candidates.',
            'image_url': './images/job-portal.jpg',
            'github': 'https://github.com/aneebnaqvi15/jobportal',
            'technologies': 'Django, HTML, CSS, JavaScript'
        },
        {
            'title': 'Restaurant Management System',
            'description': 'A complete solution for restaurant operations and order management.',
            'image_url': './images/restaurant.jpg',
            'github': 'https://github.com/aneebnaqvi15/Restaurent_Management_system',
            'technologies': 'Django, HTML, CSS, JavaScript, Tailwind'
        },
        {
            'title': 'Food App',
            'description': 'A web app for food meal planer and recipe planner.',
            'image_url': './images/food-app.jpg',
            'github': 'https://github.com/aneebnaqvi15/Food-App',
            'technologies': 'HTML, CSS, JavaScript'
        },
        {
            'title': 'NewsCaster Android App',
            'description': 'A news aggregation app that delivers personalized news content.',
            'image_url': './images/news-app.jpg',
            'github': 'https://github.com/aneebnaqvi15/NewsCaster',
            'technologies': 'Android, Java, XML, Firebase'
        },
        {
            'title': 'Portfolio Website',
            'description': 'A modern and responsive portfolio website showcasing my work.',
            'image_url': './images/portfolio.jpg',
            'github': 'https://github.com/aneebnaqvi15/portfolio-website',
            'technologies': 'HTML5, CSS3, JavaScript, GSAP'
        }
    ]
    
    for project in projects:
        FirebaseModel.objects.create(**project)

def remove_initial_projects(apps, schema_editor):
    FirebaseModel = apps.get_model('portfolio', 'FirebaseModel')
    FirebaseModel.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0006_remove_firebasemodel_image_firebasemodel_image_file_and_more'),  # Replace with your last migration name
    ]

    operations = [
        migrations.RunPython(add_initial_projects, remove_initial_projects)
    ] 