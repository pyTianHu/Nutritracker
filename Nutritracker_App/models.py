from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class BodyWeight(models.Model):
    date = models.DateField()
    bodyWeight = models.IntegerField()
    user = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.user}_{self.date}_{self.bodyWeight}"
    
    def get_bodyweight(self):
        return self.bodyWeight
    
    def get_date(self):
        return self.date
    
    def get_user(self):
        return self.user

class Goals(models.Model):
    bodyWeight_goal = models.IntegerField()
    bodyWeight_goal_deadline = models.DateField()

    def __str__(self) -> str:
        return f"{self.bodyWeight_goal}-{self.bodyWeight_goal_deadline}"
    