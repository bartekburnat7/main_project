from django.forms import ModelForm
from django.forms import widgets
from django import forms
from django.db import models 
from .models import schedule_of_lesson

class scheduleLesson(ModelForm):
    created_by_user = models.CharField()
    type_of_lesson = models.CharField()
    time_of_lesson = widgets.DateTimeInput()
    class Meta:
        model = schedule_of_lesson
        fields = ['created_by_user', 'type_of_lesson', 'time_of_lesson']