# Generated by Django 3.2.19 on 2023-11-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit_sync_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
