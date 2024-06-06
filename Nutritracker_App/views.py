from django.shortcuts import render, redirect, HttpResponse   
from .forms import AddWorkoutForm, ExerciseFormSet, AddMealForm, MealFormSet


# Create your views here.
def home(request):
    return render(request, "home.html")

def add_workout(request):
    if request.method == 'POST':
        form = AddWorkoutForm(request.POST)
        formset = ExerciseFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            workout = form.save(commit=False)
            for exercise_form in formset:
                exercise = exercise_form.cleaned_data.get('exercise')
                print(exercise)
            return redirect('home')
    else:
        form = AddWorkoutForm()
        formset = ExerciseFormSet()
    return render(request, 'add_workout.html', {'form': form, 'formset': formset})

def add_meal(request):
    if request.method == 'POST':
        form = AddMealForm(request.POST)
        formset = MealFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            foods = form.save(commit=False)
            for meal_form in formset:
                meal = meal_form.cleaned_data.get('meal')
                print(meal)
            return redirect('home')
    else:
        form = AddMealForm()
        formset = MealFormSet()
    return render(request, 'add_meal.html', {'form': form, 'formset': formset})


def add_weight(request):
    return HttpResponse("work in progress")

def set_goals(request):
    return HttpResponse("work in progress")

def add_measures(request):
    return HttpResponse("work in progress")


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