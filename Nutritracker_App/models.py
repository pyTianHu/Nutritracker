from django.db import models

# Create your models here.
class BodyWeight(models.Model):
    date = models.DateField()
    bodyWeight = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.date} - {self.bodyWeight}"
    
    def get_bodyweight(self):
        return self.bodyWeight
    
    def get_date(self):
        return self.date

class Goals(models.Model):
    bodyWeight_goal = models.IntegerField()
    bodyWeight_goal_deadline = models.DateField()

    def __str__(self) -> str:
        return f"{self.bodyWeight_goal}-{self.bodyWeight_goal_deadline}"
    