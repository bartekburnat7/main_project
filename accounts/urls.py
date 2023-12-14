from django.urls import path
from . import views

'''
Urls for the CustomUser model signup form.
'''


urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
