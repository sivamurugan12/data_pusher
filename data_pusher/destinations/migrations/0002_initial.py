# Generated by Django 5.1.7 on 2025-03-13 08:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destinations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_destinations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='destination',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_destinations', to=settings.AUTH_USER_MODEL),
        ),
    ]
