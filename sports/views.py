from django.db.models import query
from django.shortcuts import render
from .models import Sports, Player, Link
import random

# Create your views here.

def index(request):
    sports = Sports.objects.all()
    l = sports.count()
    randomPk = random.randint(1, l)
    # sport = sports.filter(pk=randomPk)
    sport = Sports.objects.get(pk=randomPk)

    context = {
        'sports': sport
    }
    return render(request, 'index.html', context)


def rules(request, pk):
    sport = Sports.objects.get(pk=pk)
    context = {
        'sports': sport
    }
    return render(request, 'sports/rules.html', context)


def notables(request, pk):
    sport = Sports.objects.get(pk=pk)
    context = {
        'sports':sport
    }
    return render(request, 'sports/notables.html', context)


def links(request, pk):
    sport = Sports.objects.get(pk=pk)
    context = {
        'sports':sport
    }
    return render(request, 'sports/link.html', context)