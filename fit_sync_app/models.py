from django.db import models 


class schedule_a_lesson(models.Model):
    # created_by_user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_lesson = models.CharField(max_length=200)
    time_of_lesson = models.DateTimeField(blank=False)