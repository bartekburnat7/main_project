from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class UserSettings(models.Model):
    user = models.OneToOneField(CustomUser, blank=False, on_delete=models.CASCADE, related_name="user")