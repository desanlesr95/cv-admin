# Generated by Django 4.2.4 on 2023-08-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_url',
            field=models.ImageField(blank=True, upload_to='users_profile'),
        ),
    ]
