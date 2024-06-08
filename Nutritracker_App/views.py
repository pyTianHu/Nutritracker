from django.shortcuts import render, redirect, HttpResponse  
import pandas as pd 
from datetime import timedelta, datetime
from .forms import AddWeightForm, SetGoalsForm
from .models import (
    BodyWeight, 
    Goals
    )

LAST_WEEK = datetime.now() - timedelta(days=7)

# Create your views here.
def home(request):
    """
    TODO: caching for bodyweight change calculations 
    """ 
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
    if request.method == "POST":
        form = AddWeightForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    elif request.method == "GET":
        form = AddWeightForm()
    return render(request, 'add_weight.html', {'form': form})

def set_goals(request):
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