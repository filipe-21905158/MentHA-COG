from django.shortcuts import render
from requests import session
from .models import Phase, Session


# Create your views here
def session_presentation(request, number):
    context = {"session": Session.objects.filter( number = number).first(),
     "phases": Phase.objects.filter( session__number = number).all().order_by("number")}
    
    return render(request, "Session_Phases/session.html", context)

def dashboard_presentation(request):
    context= {"sessions": Session.objects.all()}
    
    return render(request, "Session_Phases/dashboard.html", context)