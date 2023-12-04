from django.db import models 
from accounts.models import CustomUser

status_choices = (
    ("pending", "pending"),
    ("completed", "completed"),
    ("cancelled", "cancelled"),
)

class TrainingSession(models.Model):
    trainer = models.OneToOneField(CustomUser, blank=False, on_delete=models.CASCADE, related_name="trainer")
    student = models.CharField(max_length=256, blank=False)
    lesson_type = models.CharField(max_length=200, blank=False)
    timestamp = models.DateTimeField(blank=False)
    price = models.IntegerField(blank=False, default=0)
    status = models.CharField(max_length=200, blank=False, default="pending", choices=status_choices)