from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add_meal/", views.add_meal, name="add_meal"),
    path("add_workout/", views.add_workout, name="add_workout"),
    path("add_weight/", views.add_weight, name="add_weight"),
    path("add_measures/", views.add_measures, name="add_measures"),
    path("set_goals/", views.set_goals, name="set_goals"),
    path("about/", views.about, name= "about"),
    path("services/", views.services, name= "services"),
    path("contact/", views.contact, name= "contact"),
    path("user/", views.user, name= "user"),
    path("learnmore/", views.learnmore, name= "learnmore"),
]