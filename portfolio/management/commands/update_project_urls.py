from django.core.management.base import BaseCommand
from portfolio.models import Project

class Command(BaseCommand):
    help = 'Updates project GitHub URLs to use the correct repository'

    def handle(self, *args, **options):
        # Update all projects to use the correct GitHub URL
        Project.objects.filter(github__contains='aneebnaqvi15/portfolio').update(
            github='https://github.com/aneebnaqvi15/MyportfolioV3'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully updated project GitHub URLs')) 