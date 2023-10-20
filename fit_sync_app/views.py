from django.shortcuts import render
from django.contrib import messages
from fit_sync_app.models import schedule_of_lesson
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "index.html")

def schedule(request):
    if request.method == 'POST':
        # created_by_user = request.POST.get('created_by_user')
        current_user = request.user
        created_for_user = request.POST.get('created_for_user')
        type_of_lesson = request.POST.get('type_of_lesson')
        time_of_lesson = request.POST.get('time_of_lesson')
        try:
            form_for_user = User.objects.get(username=created_for_user)
            schedule_of_lesson.objects.create(created_by_user=current_user, created_for_user=form_for_user, type_of_lesson=type_of_lesson, time_of_lesson=time_of_lesson)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')            
    return render(request, "schedule.html")