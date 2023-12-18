from django.shortcuts import render, redirect
from django.contrib import messages
from fit_sync_app.models import TrainingSession
from accounts.models import CustomUser


'''
Render code for the homepage of the website
and the navbar which is included in all pages.
Extra pages are rendered below.
'''


def index(request):
    return render(request, "index.html")


def features(request):
    return render(request, "features_page.html")


def goals(request):
    return render(request, "goals_page.html")


def about(request):
    return render(request, "about_us_page.html")


'''
Render the 404 and 500 error pages.
'''


def handler404(request, exception):
    return render(request, "error/404.html")


def handler500(request):
    return render(request, "error/500.html")


'''
Render html for the trainer dashboard which
includes code for the calendar and the earnings.
'''


def dashboard(request):
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result
    current_user = request.user
    query = TrainingSession.objects.filter(trainer=current_user)
    query = query.order_by('timestamp')
    context = {'query': query,
               'dashboard_error': GetLesson(query),
               'lesson_count': GetLessonCount(query),
               'total_price': LessonTotalPrice(query),
               'fee_price': "{:0.2f}".format(LessonTotalPrice(query) * 0.9)}
    return render(request, "dashboard.html", context)


'''
Render html for the student dashboard which
includes code for the calendar and the incoming
lessons.
'''


def student_dashboard(request):
    user = request.user
    if user.is_trainer is True:
        return redirect("dashboard")
    query = TrainingSession.objects.filter(student=user,
                                           status="accepted")
    query = query.order_by('timestamp')
    incoming_lessons = TrainingSession.objects.filter(student=user,
                                                      status="pending")
    incoming_lessons = incoming_lessons.order_by('timestamp')
    context = {'query': query,
               'dashboard_error': GetLesson(query),
               'incoming_error': GetLesson(incoming_lessons),
               'incoming_lessons': incoming_lessons}
    return render(request, "student_dashboard.html", context)


'''
Function to accept a lesson request from a trainer.
'''


def AcceptLesson(request, lesson_id):
    accept_lesson = TrainingSession.objects.get(id=lesson_id)
    if request.user != accept_lesson.student:
        return redirect("student_dashboard")
    accept_lesson.status = "accepted"
    accept_lesson.save()
    trainer_username = accept_lesson.trainer.username
    message = "Lesson from @" + trainer_username + " accepted successfully!"
    messages.add_message(request, messages.SUCCESS, message)
    return redirect("student_dashboard")


'''
Function to cancel a lesson request from a trainer.
'''


def CancelLesson(request, lesson_id):
    cancel_lesson = TrainingSession.objects.get(id=lesson_id)
    if request.user != cancel_lesson.student:
        return redirect("student_dashboard")
    cancel_lesson.status = "cancelled"
    cancel_lesson.save()
    trainer_username = cancel_lesson.trainer.username
    message = "Lesson from @" + trainer_username + " has been cancelled!"
    messages.add_message(request, messages.WARNING, message)
    return redirect("student_dashboard")


'''
Render html for the trainer dashboard which
includes the form to create a new lesson and
the list of lessons.
'''


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
                price=price)
            student_user = student.username
            message = "Lesson for @" + student_user + " created successfully"
            messages.add_message(request, messages.SUCCESS, message)
        except CustomUser.DoesNotExist:
            form_error = "User does not exist"
    query = TrainingSession.objects.filter(trainer=current_user)
    query = query.order_by('timestamp')
    context = {'query': query,
               'dashboard_error': GetLesson(query),
               'form_error': form_error}
    return render(request, "schedule.html", context)


'''
Function to delete a lesson request from a trainer.
'''


def DeleteLesson(request, lesson_id):
    current_user = request.user
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result
    lesson = TrainingSession.objects.get(id=lesson_id)
    if current_user != lesson.trainer:
        return redirect("schedule")
    lesson.delete()
    student_user = lesson.student.username
    message = "Lesson for @" + student_user + " deleted successfully"
    messages.add_message(request, messages.WARNING, message)
    return redirect("schedule")


'''
Render html for the trainers which includes
the form to edit the lesson.
'''


def EditLesson(request, lesson_id):
    current_user = request.user
    edit_lesson = TrainingSession.objects.get(id=lesson_id)
    auth_result = AuthCheck(request)
    if auth_result:
        return auth_result
    if current_user != edit_lesson.trainer:
        return redirect("schedule")
    if request.method == 'POST':
        student = request.POST.get('created_for_user')
        lesson_type = request.POST.get('type_of_lesson')
        time = request.POST.get('time_of_lesson')
        price = request.POST.get('price_of_lesson')
        try:
            get_student = CustomUser.objects.get(username=student)
            edit_lesson.student = get_student
            edit_lesson.lesson_type = lesson_type
            edit_lesson.timestamp = time
            edit_lesson.price = price
            edit_lesson.save()
            message = "Lesson for @" + get_student.username + " saved!"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect("schedule")
        except CustomUser.DoesNotExist:
            message = "@" + student + " does not exist."
            messages.add_message(request, messages.ERROR, message)
            redirect("update_lesson/lesson_id")
    return render(request, "update_lesson.html", {'edit_lesson': edit_lesson})


'''
Function to check if the user is logged in
and if they are a trainer which redirects
them accordingly.
'''


def AuthCheck(request):
    if not request.user.is_authenticated:
        return redirect("account_login")
    elif request.user.is_trainer is False:
        return redirect("student_dashboard")


'''
Function to check if the trainer has any lessons
and if not, returns an error message.
'''


def GetLesson(input):
    if input.count() == 0:
        error = "No lessons found"
        return error
    else:
        error = ""
        return error


'''
Function to count the number of lessons.
'''


def GetLessonCount(input):
    return input.count()


'''
Function to calculate the total price
of the lessons.
'''


def LessonTotalPrice(input):
    total = 0
    for i in input:
        total = total + i.price
    return total
