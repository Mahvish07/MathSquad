from django.shortcuts import render

# Create your views here. 
    
def productDetails(request):

    return render(request, "product_Details.html")