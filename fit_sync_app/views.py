from django.shortcuts import render, redirect
from django.contrib import messages
from fit_sync_app.models import TrainingSession
from accounts.models import CustomUser


# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result    
    current_user = request.user
    query = TrainingSession.objects.filter(trainer=current_user).order_by('timestamp')
    return render(request, "dashboard.html", {'query': query,
                                              'dashboard_error': GetLesson(query),
                                              'lesson_count': GetLessonCount(query),
                                              'total_price': LessonTotalPrice(query),})

def student_dashboard(request):
    current_user = request.user
    query = TrainingSession.objects.filter(trainer=current_user).order_by('timestamp')
    return render(request, "student_dashboard.html", {'query': query})

def schedule(request):
    current_user = request.user
    form_error = ""
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result
    
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
            form_error = "User does not exist"
        
    query = TrainingSession.objects.filter(trainer=current_user).order_by('timestamp')
                    
    return render(request, "schedule.html", {'query': query, 'dashboard_error': GetLesson(query), 'form_error': form_error,})

def DeleteLesson(request, lesson_id):
    current_user = request.user
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result
    lesson = TrainingSession.objects.get(id=lesson_id)
    if current_user != lesson.trainer:
        return redirect("schedule")
    lesson.delete()
    return redirect("schedule")

def EditLesson(request, lesson_id):
    current_user = request.user
    editlesson = TrainingSession.objects.get(id=lesson_id)
    
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result
    
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

def AuthCheck(request):
    if not request.user.is_authenticated:
        return redirect("account_login")
    elif request.user.is_trainer == False:
        return redirect("student_dashboard")

def GetLesson(input):
    if input.count() == 0:
        error =  "No lessons found"
        return error
    else:
        error = ""
        return error

def GetLessonCount(input):
    return input.count()

def LessonTotalPrice(input):
    total = 0
    for i in input:
        total = total + i.price
    return total
