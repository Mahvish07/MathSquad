from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from .views import  contest, rewardsachievement, questions

urlpatterns = [
    path("", TemplateView.as_view(template_name='index.html'), name="home"),
    path("login/", TemplateView.as_view(template_name='login.html'), name="about"),
    path("register/", TemplateView.as_view(template_name='register.html'), name="register"),
    path("contest/", contest, name="contest"),
    path("achievement/", rewardsachievement, name="achievement"),
    path("browse/", contest, name="browse"),
    path("category/", contest, name="category"),
    path("community/", contest, name="community"),
    path("feedback/", contest, name="feedback"),
    path("layout/", contest, name="layout"),
    path("notification/", contest, name="notification"),
    path("leaderboard/", contest, name="leaderboard"),
    path("profile/", contest, name="profile"),
    path("navigation/", contest, name="navigation"),
    path("questions/", questions, name="questions"),
    # path('problem-solving/', problemsolvingmodule, name='problem_solving_module'),

]

