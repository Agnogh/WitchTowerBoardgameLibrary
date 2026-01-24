# No need for this - QueryDict has urlencode build in
# from urllib.parse import urlencode
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

    # QueryDict
    params = request.GET.copy()
    # page number
    params.pop("page", None)
    # to convert dictionary to URL query string
    preserved_qs = params.urlencode()

    # Sort UI helprs
    is_price_asc = sort == "price"
    is_price_desc = sort == "-price"

    # Clicking the price sort toggles direction
    price_toggle_sort = "-price" if is_price_asc else "price"

    context = {
        "games": page_obj,  # loops over current page, not all games
        "page_obj": page_obj,
        "query": query,
        "sort": sort,
        "games_count": games.count(),
        "preserved_qs": preserved_qs,
        # starting number for the current page (1 for 1st page, 7 for 2nd page)
        "start_index": page_obj.start_index(),
        # end number for current page (6 for 1st page, 12 for 2nd page...)
        "end_index": page_obj.end_index(),
        # number of items on all pages
        "total_count": page_obj.paginator.count,
        # sort lower to higher price
        "is_price_asc": is_price_asc,
        # from higer to lower price
        "is_price_desc": is_price_desc,
        # revert if ascending or descending or sort price if none selected
        "price_toggle_sort": price_toggle_sort,
    }

    return render(request, "games/game_list.html", context)
