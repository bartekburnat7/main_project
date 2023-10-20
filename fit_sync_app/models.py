from django.db import models 
from django.contrib.auth.models import User

class schedule_of_lesson(models.Model):
    created_by_user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name='created_by_user')
    created_for_user = models.CharField(max_length=256, blank=False)
    type_of_lesson = models.CharField(max_length=200, blank=False)
    time_of_lesson = models.DateTimeField(blank=False)