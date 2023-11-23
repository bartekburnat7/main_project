from django.shortcuts import render, redirect
from django.contrib import messages
from fit_sync_app.models import TrainingSession
from accounts.models import CustomUser


# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("account_login")
    current_user = request.user
    query = TrainingSession.objects.filter(trainer=current_user).order_by('timestamp')
    return render(request, "dashboard.html", {'query': query})

def schedule(request):
    current_user = request.user
    if not request.user.is_authenticated:
        return redirect("account_login")
    
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

def DeleteLesson(request, lesson_id):
    current_user = request.user
    if not request.user.is_authenticated:
        return redirect("account_login")
    lesson = TrainingSession.objects.get(id=lesson_id)
    if current_user != lesson.trainer:
        return redirect("schedule")
    lesson.delete()
    return redirect("schedule")

def EditLesson(request, lesson_id):
    current_user = request.user
    editlesson = TrainingSession.objects.get(id=lesson_id)
    
    if current_user != editlesson.trainer:
        return redirect("schedule")
    
    if request.method == 'POST':
        student = request.POST.get('created_for_user')
        lesson_type = request.POST.get('type_of_lesson')
        time = request.POST.get('time_of_lesson')
        price = request.POST.get('price_of_lesson')
        try:
            CustomUser.objects.get(username=student)
            editlesson.student = student
            editlesson.lesson_type = lesson_type
            editlesson.timestamp = time
            editlesson.price = price
            editlesson.save()
            return redirect("schedule")
        except CustomUser.DoesNotExist:
            return render(request, "update_lesson.html", {'error': "User does not exist"})
    
    return render(request, "update_lesson.html", {'editlesson': editlesson})