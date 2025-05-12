from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import contest, rewardsachievement, contestprizes, register_contest, my_registered_contests, attempt_contest

urlpatterns = [
    # path("", TemplateView.as_view(template_name='index.html'), name="home"),
    # path("login/", TemplateView.as_view(template_name='login.html'), name="about"),
    # path("register/", TemplateView.as_view(template_name='register.html'), name="register"),
    path("my-contests/", my_registered_contests, name="my_registered_contests"),
    path("contest/", contest, name="contest"),
    path("achievement/", rewardsachievement, name="achievement"),
    # path("browse/", browse, name="browse"),
    # path("category/", category, name="category"),
    # path("community/", commu
    # 
    # 
    # 
    # 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ---
    
    
    
    nity, name="community"),
    path("feedback/", contest, name="feedback"),
    path("layout/", contest, name="layout"),
    path("notification/", contest, name="notification"),
    path("leaderboard/", contest, name="leaderboard"),
    path("profile/", contest, name="profile"),
    path("navigation/", contest, name="navigation"),
    # path('contest/<int:contest_id>/prizes/', contestprizes, name='contest_prizes'),  # Fixed this line
    path('register-contest/', register_contest, name='register_contest'),
    path('contest/<int:contest_id>/attempt/', attempt_contest, name='attempt_contest'),
]
