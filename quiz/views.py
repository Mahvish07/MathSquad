from django.shortcuts import render, get_object_or_404, redirect
from .models import Contest, Question, Prizes
from .forms import RegistrationForm

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

def contestprizes(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    prizes = Prizes.objects.filter(contest=contest)
    return render(request, "contest_prizes.html", {"contest": contest, "prizes": prizes})

def register_contest(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the registration to the database
            return redirect('register_contest')  # Redirect to the same page after successful registration
    else:
        form = RegistrationForm()

    contests = Contest.objects.all()  # Fetch all contests from the database
    return render(request, "register_contest.html", {"contests": contests, "form": form})