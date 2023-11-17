from django.urls import path , include
from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
]
