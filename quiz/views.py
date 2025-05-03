from django.shortcuts import render
from .models import Contest
from .models import Question
from .models import Problem  # Replace 'Problem' with the actual model name for problem-solving challenges

# Create your views here. 
    
def adminPanel(request):

    return render(request, "admin_panel.html")
# Create your views here. 
    
def categoryPage(request):

    return render(request, "category-page.html")


# Create your views here. 
    
def communityDiscussion(request):

    return render(request, "community_discussion.html")


# Create your views here. 

def contest(request):
    contests = Contest.objects.all()  # Fetch all contests from the database
    return render(request, "contest.html", {"contests": contests})







    

# Create your views here. 
    
def index(request):

    return render(request, "index.html")

# Create your views here. 
    
def instancefeadback(request):

    return render(request, "instance_feadback.html")

# Create your views here. 
    
def notificationreminder(request):

    return render(request, "notification-reminder.html")


# Create your views here. 
    
def profilemanagment(request):

    return render(request, "profile_management.html")

# Create your views here. 
    
def rewardsachievement(request):

    return render(request, "rewards_achievement.html")

# Create your views here. 
    
def updateleaderboard(request):

    return render(request, "update_leaderboard.html")

def questions(request):
    questions = Question.objects.all()  # Fetch all questions from the database
    return render(request, "contest_questions.html", {"questions": questions})
    return render(request, "questions.html")

def problem_solving_module(request):
    problems = Problem.objects.all()  # Fetch all problem-solving challenges from the database
    return render(request, "problem_solving_module.html", {"problems": problems})
