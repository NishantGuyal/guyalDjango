from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FootballPlayers, PlayerTeams
from .forms import PlayerTeamsForm


def home(request):
    players = FootballPlayers.objects.all()
    return render(request, "home.html", {"players": players})


def player_detail(request, player_id):
    player = get_object_or_404(FootballPlayers, pk=player_id)
    return render(request, "player_detail.html", {"player": player})


def player_store_view(request):
    teams = None
    if request.method == "POST":
        form = PlayerTeamsForm(request.POST)
        if form.is_valid():
            player_team = form.cleaned_data["player_teams"]
            teams = PlayerTeams.objects.filter(
                players=player_team
            ) 
    else:
        form = PlayerTeamsForm()

    return render(request, "team_form.html", {"teams": teams, "form": form})


def about(response):
    return HttpResponse("Welcome to About page")


def contact(response):
    return HttpResponse("Welcome to Contact page")
