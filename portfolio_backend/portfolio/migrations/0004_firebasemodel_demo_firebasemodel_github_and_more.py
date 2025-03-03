# Generated by Django 5.1.4 on 2025-02-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_firebasemodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='firebasemodel',
            name='demo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='firebasemodel',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='firebasemodel',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='firebasemodel',
            name='technologies',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
