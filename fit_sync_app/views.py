from django.shortcuts import render
from django.contrib import messages
from fit_sync_app.models import TrainingSession
from accounts.models import CustomUser


# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

def schedule(request):
    current_user = request.user
    if request.method == 'POST':
        student = request.POST.get('created_for_user')
        lesson_type = request.POST.get('type_of_lesson')
        time = request.POST.get('time_of_lesson')
        price = request.POST.get('price_of_lesson')
        try:
            student = CustomUser.objects.get(username=student)
            TrainingSession.objects.create(
                trainer=current_user,
                student=student,
                lesson_type=lesson_type,
                timestamp=time,
                price=price
                )
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist')
        
    query = TrainingSession.objects.filter(trainer=current_user).order_by('timestamp')
                    
    return render(request, "schedule.html", {'query': query})