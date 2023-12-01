"""fit_sync URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from django.contrib import admin
from django.urls import path , include
from fit_sync_app import views

from allauth.account.views import signup, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("account/signup/", signup, name="account_signup"),
    path("account/login/", login, name="account_login"),
    path("account/logout/", logout, name="account_logout"),
    path('', views.index, name='home'),
    path('schedule/', views.schedule, name='schedule'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('schedule/<lesson_id>', views.DeleteLesson, name='deletelesson'),
    path('update_lesson/<lesson_id>', views.EditLesson, name='editlesson'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
