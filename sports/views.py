from django.db.models import query
from django.shortcuts import render
from .models import Sports, Player, Link

# Create your views here.

def index(request):
    sports = Sports.objects.all()
    context = {
        'sports': sports
    }
    return render(request, 'index.html', context)


def rules(request):
    context = {}
    return render(request, 'sports/rules.html', context)