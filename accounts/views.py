from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

'''
Render the signup page and handle the
signup form and redirect to the dashboard.
Also return errors if the form is invalid.
'''


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, "account/signup.html", {'form': form.errors})
