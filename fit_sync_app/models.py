from django.db import models 
from django.contrib.auth.models import User

class schedule_of_lesson(models.Model):
    created_by_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    type_of_lesson = models.CharField(max_length=200, blank=False)
    time_of_lesson = models.DateTimeField(blank=False)