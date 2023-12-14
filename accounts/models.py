from django.contrib.auth.models import AbstractUser
from django.db import models

'''
A custom user model that extends the AbstractUser model.
'''


class CustomUser(AbstractUser):
    is_trainer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


'''
A model for user settings for further customization
in the future.
'''


class UserSettings(models.Model):
    user = models.OneToOneField(CustomUser,
                                blank=False,
                                on_delete=models.CASCADE,
                                related_name="user")
