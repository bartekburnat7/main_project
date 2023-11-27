from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import SignupForm
from fit_sync_app import views
from accounts.models import CustomUser

def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, "signup.html", {'form': form.errors})