from django.shortcuts import render, get_object_or_404
from .models import Beer
# Create your views here.

def menu(request):
    beers = Beer.objects.all()
    return render(request, 'menu/menu.html', {'beers': beers})

def home(request):
    return render(request, 'menu/home.html')
