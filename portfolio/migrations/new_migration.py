from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0006_remove_firebasemodel_image_firebasemodel_image_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('github', models.URLField(blank=True, null=True)),
                ('technologies', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ] 