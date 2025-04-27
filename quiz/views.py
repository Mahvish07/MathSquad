from django.shortcuts import render

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

    return render(request, "contest.html")

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
    
def problemsolvingmodule(request):

    return render(request, "problem-solvingModule.html")

# Create your views here. 
    
def profilemanagment(request):

    return render(request, "profile-management.html")

# Create your views here. 
    
def rewardsachievement(request):

    return render(request, "rewards-achievement.html")

# Create your views here. 
    
def updateleaderboard(request):

    return render(request, "update_leaderboard.html")