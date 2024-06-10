from django.shortcuts import render, redirect, HttpResponse  
from django.contrib.auth import (authenticate, login as auth_login, logout)
import pandas as pd 
from datetime import timedelta, datetime
from .custom_context_processor import get_username

from .forms import (
    AddWeightForm, 
    SetGoalsForm, 
    CustomUserCreationForm,
    CustomAuthenticationForm
    )

from .models import (
    BodyWeight, 
    Goals,
    )

LAST_WEEK = datetime.now() - timedelta(days=7)

def register(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, "register.html", {'form': form})
    elif request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "register.html", {'form': form})
    

def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request,"home.html")
    else:
        form = CustomAuthenticationForm()
        return render(request, "login.html", {'form': form})
    return render(request,"home.html")


def log_out(request):
    logout(request)
    return redirect('log_out')


# Create your views here.
def home(request):
    """
    TODO: caching for bodyweight change calculations 
    TODO: filter for username in all queries
    """ 
    username = request.current_username
    if not username :
        return redirect("login")
    else:
        goals = Goals.objects.all()
        weights = BodyWeight.objects.filter(date__gte=LAST_WEEK).values('date', 'bodyWeight').order_by('-date')
        weights_df = pd.DataFrame(weights)
        weights = weights_df.to_dict(orient='records')
        bodyweight_vs_goal = {'current_bodyweight':109, 'bodyweight_goal': 95}
        return render(request, 'home.html', {'weights': weights, 'goals':goals, 'bodyweight_vs_goal': bodyweight_vs_goal})


def add_workout(request):
    return render(request, 'add_workout.html')

def add_meal(request):
    return render(request, 'add_meal.html')


def add_weight(request):
    """
    TODO: add username to all queries
    """
    username = request.current_username
    if not username :
        return redirect("login")
    else:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('home')
        elif request.method == "GET":
            form = AddWeightForm()
        return render(request, 'add_weight.html', {'form': form})

def set_goals(request):
    """
    TODO: add username to all queries
    """
    username = request.current_username
    if not username :
        return redirect("login")
    else:
        if request.method=="POST":
            form = SetGoalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        elif request.method == "GET":
            form = SetGoalsForm()
        return render(request, 'set_goals.html', {"form": form})

def add_measures(request):
    return render(request, 'add_measures.html')


def about(request):

    return render(request, "about.html")

def services(request):

    return render(request, "services.html")

def contact(request):

    return render(request, "contact.html")

def user(request):

    return render(request, "user.html")

def learnmore(request):

    return render(request, "learnmore.html")