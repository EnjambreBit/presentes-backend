from django.shortcuts import render
from backend import settings

def home(request):
    version = settings.VERSION_NUMBER
    return render(request, 'home.html', {"version": version})
