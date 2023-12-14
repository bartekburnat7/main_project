from django.contrib import admin
from fit_sync_app.models import TrainingSession

'''
Register the TrainingSession model with the admin site
to allow for easy viewing and editing of the model's data.
'''
admin.site.register(TrainingSession)
