from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from .views import adminPanel, categoryPage, communityDiscussion, contest, index, instancefeadback, notificationreminder, problemsolvingmodule, profilemanagment, rewardsachievement, questions

urlpatterns = [
    path("", TemplateView.as_view(template_name='index.html'), name="home"),
    path("login/", TemplateView.as_view(template_name='login.html'), name="about"),
    path("register/", TemplateView.as_view(template_name='register.html'), name="register"),
    path("contest/", contest, name="contest"),
    path("achievement/", rewardsachievement, name="contest"),
    path("browse/", contest, name="contest"),
    path("category/", contest, name="contest"),
    path("community/", contest, name="contest"),
    path("feedback/", contest, name="contest"),
    path("layout/", contest, name="contest"),
    path("notification/", contest, name="contest"),
    path("problem_solving/", contest, name="contest"),
    path("leaderboard/", contest, name="contest"),
    path("profile/", contest, name="contest"),
    path("navigation/", contest, name="contest"),
    path("questions/", questions, name="contest"),



]

