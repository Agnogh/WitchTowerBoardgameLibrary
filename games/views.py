from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Game


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, "games/game_details.html", {"game": game})


def game_list(request):
    games = Game.objects.all()
    return render(request, "games/game_list.html", {"games": games})
