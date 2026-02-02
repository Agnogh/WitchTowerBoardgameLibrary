# No need for this - QueryDict has urlencode build in
# from urllib.parse import urlencode
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# don't need this anymore ->
# from django.db.models import Q


# Create your views here.

from .models import Game
# import category
from .models import Category

from django.db.models import Count, Q  # 'q' for stock filter


def category_counts_page(request):
    categories = Category.objects.annotate(
        game_count=Count("games", filter=Q(games__stock__gt=0), distinct=True)
    ).order_by("name")

    return render(request,
                  "witch_tower_boardgame_library/category_counts.html",
                  {"categories": categories})


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, "games/game_details.html", {"game": game})


# can render games & games/category/<type>
def game_list(request, category_slug=None):
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "title")
    get_category = request.GET.get("category", "").strip()
    # read games that in stock
    in_stock = request.GET.get("in_stock") == "1"

    games = Game.objects.all()
    # rule for showing games in stock
    if in_stock:
        games = games.filter(stock__gt=0)

    # If user used dropdown ?category=... on games, then
    # redirect to SEO URL /games/category/<type>
    if not category_slug and get_category:
        base_path = reverse("game_list_by_category", args=[get_category])

        params = request.GET.copy()
        params.pop("category", None)
        params.pop("page", None)  # reset pagination when category type changes
        qs = params.urlencode()

        return redirect(f"{base_path}?{qs}" if qs else base_path)

    # Apply category from the URL path
    if category_slug:
        games = games.filter(category__slug=category_slug)

    # What is currently active in search filter
    active_category_name = None
    if category_slug:
        active_category = Category.objects.filter(slug=category_slug).first()
        active_category_name = (
            active_category.name if active_category else category_slug
        )

    # search
    if query:
        games = games.filter(title__icontains=query)

    # sorting
    if sort == "price":
        games = games.order_by("price")
    elif sort == "-price":
        games = games.order_by("-price")
    else:
        games = games.order_by("title")

    # pagination
    paginator = Paginator(games, 6)  # for starter 6 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # QueryDict
    params = request.GET.copy()
    # page number
    params.pop("page", None)

    params.pop("category", None)

    # used for pagination links
    preserved_qs = params.urlencode()

    # Preserved filtres for sort links
    # used for sorting links (exclude sort itself)
    base_params = request.GET.copy()
    base_params.pop("page", None)
    base_params.pop("sort", None)
    base_params.pop("category", None)
    base_qs = base_params.urlencode()

    # Sort UI helprs
    is_price_asc = sort == "price"
    is_price_desc = sort == "-price"

    # Clicking the price sort toggles direction
    price_toggle_sort = "-price" if is_price_asc else "price"

    # base list url
    list_url = (
        reverse("game_list_by_category", args=[category_slug])
        if category_slug
        else reverse("game_list")
    )

    def build_qs(overrides=None, remove=None):
        params = request.GET.copy()
        params.pop("page", None)  # always reset pagination when filters change

        if remove:
            for key in remove:
                params.pop(key, None)

        if overrides:
            for key, value in overrides.items():
                if value in (None, "", False):
                    params.pop(key, None)
                else:
                    params[key] = value

        qs = params.urlencode()
        return f"{list_url}?{qs}" if qs else list_url

    remove_search_url = build_qs(remove=["q"])
    remove_category_url = build_qs(remove=["category"])
    remove_in_stock_url = build_qs(remove=["in_stock"])
    remove_sort_url = build_qs(overrides={"sort": "title"})
    clear_all_url = reverse("game_list")

    context = {
        "games": page_obj,  # loops over current page, not all games
        "page_obj": page_obj,
        "query": query,
        "sort": sort,
        "preserved_qs": preserved_qs,
        # pagination
        "base_qs": base_qs,
        # sort lower to higher price
        "is_price_asc": is_price_asc,
        # from higer to lower price
        "is_price_desc": is_price_desc,
        # revert if ascending or descending or sort price if none selected
        "price_toggle_sort": price_toggle_sort,
        "list_url": list_url,
        # this so for categories
        "categories": (
            Category.objects.annotate(
                game_count=Count("games", filter=Q(games__stock__gt=0),
                                 distinct=True)
            ).order_by("name")
        ),
        "category_slug": category_slug,
        "games_count": games.count(),
        # starting number for the current page (1 for 1st page, 7 for 2nd page)
        "start_index": page_obj.start_index(),
        # end number for current page (6 for 1st page, 12 for 2nd page...)
        "end_index": page_obj.end_index(),
        # number of items on all pages
        "total_count": page_obj.paginator.count,
        "in_stock": in_stock,
        # active category search
        "active_category_name": active_category_name,
        # removes search criteria based on the word/term
        "remove_search_url": remove_search_url,
        # removes category only from search
        "remove_category_url": remove_category_url,
        # remove only if product is in store
        "remove_in_stock_url": remove_in_stock_url,
        # returs sort back to 'title'
        "remove_sort_url": remove_sort_url,
        # removes all seacrh criterias
        "clear_all_url": clear_all_url,
    }

    return render(request, "games/game_list.html", context)
