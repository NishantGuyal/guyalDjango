from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FootballPlayers


def home(request):
    players = FootballPlayers.objects.all()
    return render(request, "home.html", {"players": players})


def player_detail(request, player_id):
    player = get_object_or_404(FootballPlayers, pk=player_id)
    return render(request, "player_detail.html", {"player": player})


def about(response):
    return HttpResponse("Welcome to About page")


def contact(response):
    return HttpResponse("Welcome to Contact page")
