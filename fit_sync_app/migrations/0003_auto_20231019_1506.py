# Generated by Django 3.2.19 on 2023-10-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit_sync_app', '0002_schedule_of_lesson_cretaed_for_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule_of_lesson',
            name='cretaed_for_user',
        ),
        migrations.AddField(
            model_name='schedule_of_lesson',
            name='created_for_user',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]
