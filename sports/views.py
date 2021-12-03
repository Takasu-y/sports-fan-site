from django.shortcuts import render, get_object_or_404, get_list_or_404
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
    sport = get_object_or_404(Sports, pk=pk)
    context = {
        'sports': sport
    }
    return render(request, 'sports/rules.html', context)


def notables(request, pk):
    sport = get_object_or_404(Sports, pk=pk)
    players = get_list_or_404(Player, sports__name=sport.name)

    context = {
        'sports':sport,
        'players':players
    }
    return render(request, 'sports/notables.html', context)


def playerDetail(request, pk, name):
    sport = get_object_or_404(Sports, pk=pk)
    player = get_object_or_404(Player, name=name)
    print(player)
    context = {
        'sports': sport,
        'player': player
    }
    return render(request, "sports/detail.html", context)

def links(request, pk):
    sport = get_object_or_404(Sports, pk=pk)
    links = get_list_or_404(Link, sports__name=sport.name)

    context = {
        'sports': sport,
        'links':links
    }
    return render(request, 'sports/link.html', context)