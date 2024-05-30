from django import forms
from django.forms import formset_factory

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