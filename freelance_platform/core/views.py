from django.shortcuts import render, redirect
from .forms import ProjectForm, BidForm
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'core/home.html', {'projects': projects})

def post_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'core/post_project.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'core/profile.html')