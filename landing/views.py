from django.shortcuts import render

# Create your views here.
def showLanding(request):
    return render(request, "landing.html")