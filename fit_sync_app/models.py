from django.db import models 
from accounts.models import CustomUser

'''
Choices for the status of a lesson.
'''
status_choices = (
    ("pending", "pending"),
    ("accepted", "accepted"),
    ("cancelled", "cancelled"),
)

'''
Model for a training sessions.
'''
class TrainingSession(models.Model):
    trainer = models.ForeignKey(CustomUser, blank=False, on_delete=models.CASCADE, related_name="trainer")
    student = models.ForeignKey(CustomUser, blank=False, on_delete=models.CASCADE, related_name="student")
    lesson_type = models.CharField(max_length=200, blank=False)
    timestamp = models.DateTimeField(blank=False)
    price = models.IntegerField(blank=False, default=0)
    status = models.CharField(max_length=200, blank=False, default="pending", choices=status_choices)