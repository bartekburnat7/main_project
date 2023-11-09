from django.db import models 
from django.contrib.auth.models import User


class TrainingSession(models.Model):
    trainer = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="trainer")
    student = models.CharField(max_length=256, blank=False)
    lesson_type = models.CharField(max_length=200, blank=False)
    timestamp = models.DateTimeField(blank=False)