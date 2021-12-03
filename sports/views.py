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
    players = Player.objects.filter(sports__name=sport.name)

    context = {
        'sports':sport,
        'players':players
    }
    return render(request, 'sports/notables.html', context)


def playerDetail(request, pk, name):
    sport = Sports.objects.get(pk=pk)
    player = Player.objects.get(name=name)
    print(player)
    context = {
        'sports': sport,
        'player': player
    }
    return render(request, "sports/detail.html", context)

def links(request, pk):
    sport = Sports.objects.get(pk=pk)
    links = Link.objects.filter(sports__name=sport.name)

    context = {
        'sports': sport,
        'links':links
    }
    return render(request, 'sports/link.html', context)