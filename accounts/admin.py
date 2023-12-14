from django.contrib import admin
from .models import CustomUser, UserSettings

'''
Register the CustomUser model with the admin site.
'''


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_trainer')

admin.site.register(UserSettings)
