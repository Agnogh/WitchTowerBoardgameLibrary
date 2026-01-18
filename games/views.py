from django.core.paginator import Paginator


from django.shortcuts import render, get_object_or_404
# don't need this anymore ->
# from django.db.models import Q


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
        games = games.filter(title__icontains=query)

    if sort == "price":
        games = games.order_by("price")
    elif sort == "-price":
        games = games.order_by("-price")
    else:
        games = games.order_by("title")

    paginator = Paginator(games, 6)  # for starter 6 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "games": page_obj,  # loops over current page, not all games
        "page_obj": page_obj,
        "query": query,
        "sort": sort,
        "games_count": games.count(),
    }

    return render(request, "games/game_list.html", context)
