from django.db import models 
from django.contrib.auth.models import User

class Scheduled_Lessons_Main(models.Model):
    created_for_user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_lesson = models.TextChoices("Schedule Lesson","Online Lesson")
    time_and_date = models.DateTimeField()
