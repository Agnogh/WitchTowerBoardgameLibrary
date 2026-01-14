from django.shortcuts import render, get_object_or_404
from django.db.models import Q


# Create your views here.

from .models import Game


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, "games/game_details.html", {"game": game})


def game_list(request):
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "title")

    games = Game.objects.all()

    if query:
        games = games.filter(Q(title__icontains=query))

    if sort == "price":
        games = games.order_by("price")
    elif sort == "-price":
        games = games.order_by("-price")
    else:
        games = games.order_by("title")

    context = {
        "games": games,
        "query": query,
        "sort": sort,
    }

    return render(request, "games/game_list.html", context)
