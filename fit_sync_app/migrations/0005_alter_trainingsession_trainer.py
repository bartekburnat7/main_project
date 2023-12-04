# Generated by Django 3.2.19 on 2023-12-04 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fit_sync_app', '0004_trainingsession_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsession',
            name='trainer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL),
        ),
    ]
