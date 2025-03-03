# Generated by Django 5.1.4 on 2025-02-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_firebasemodel_demo_alter_firebasemodel_github_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firebasemodel',
            name='image',
        ),
        migrations.AddField(
            model_name='firebasemodel',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
        migrations.AddField(
            model_name='firebasemodel',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='firebasemodel',
            name='github',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='firebasemodel',
            name='technologies',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
