from django import forms
from django.forms import formset_factory
from .models import (
    BodyWeight, 
    Goals,
    User
    )

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']   


class AddWeightForm(forms.ModelForm):
    class Meta:
        model = BodyWeight
        fields = ['date', 'bodyWeight']

class SetGoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['bodyWeight_goal', 'bodyWeight_goal_deadline']

class AddWorkoutForm(forms.Form):
    # Define fields for adding a workout (e.g., date, duration, exercise, etc.)
    date = forms.DateField()
    exercise = forms.CharField()

ExerciseFormSet = formset_factory(AddWorkoutForm, extra=1) 
    
class AddMealForm(forms.Form):
    # Define fields for adding a workout (e.g., date, duration, exercise, etc.)
    date = forms.DateField()
    Food = forms.CharField()
    Amount = forms.FloatField()

MealFormSet = formset_factory(AddMealForm, extra=1) 