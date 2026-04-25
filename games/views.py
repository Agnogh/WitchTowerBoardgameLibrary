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
# import review
from .models import Review

from .forms import ReviewForm

from django.db.models import Count, Q  # 'q' for stock filter

from django.contrib.auth.decorators import login_required
# import messages (for user)
from django.contrib import messages


def category_counts_page(request):
    categories = Category.objects.annotate(
        game_count=Count("games", filter=Q(games__stock__gt=0), distinct=True)
    ).order_by("name")

    return render(request,
                  "witch_tower_boardgame_library/category_counts.html",
                  {"categories": categories})


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    # get all reviews for that post
    reviews = game.reviews.select_related("user").all()

    # chek if there is already post from logged in user (failsafe)
    existing_review = None
    if request.user.is_authenticated:
        existing_review = Review.objects.filter(
            game=game,
            user=request.user
        ).first()

    # show page & form or process submited data
    if request.method == "POST" and "review_submit" in request.POST:
        # trying to post without loged in -> send log in request (failsafe)
        if not request.user.is_authenticated:
            # instructions for user
            messages.info(request, "Log in to leave a review.")
            return redirect("login")

        # prevent additional review (failsafe)
        if existing_review:
            # explanation for user
            messages.info(request, "You reviewed this game already.")
            return redirect("game_detail", slug=game.slug)

        # build form from submited data
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # add review to that open game
            review.game = game
            # link reivew to loged in user
            review.user = request.user
            # save to database
            review.save()
            # review confirmation for user
            messages.success(request, "Review was added successfully.")
            # reload page after done (failsafe from duplcates)
            return redirect("game_detail", slug=game.slug)
    else:
        form = ReviewForm()

    context = {
        "game": game,
        "reviews": reviews,
        "review_form": form,
        "existing_review": existing_review,
    }

    return render(request, "games/game_details.html", context)


# need to be loged in
@login_required
def review_edit(request, review_id):
    # look for review + id need to match + user logged in to avoid 404
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == "POST":
        # use submited form but apply over existng
        form = ReviewForm(request.POST, instance=review)
        # if form is good (rating == num, mandatoy fileds populated)
        if form.is_valid():
            # save updated value
            form.save()
            # review update sucess for user
            messages.success(request, "Review was updated successfully.")
            # go back to 'game details' page
            return redirect("game_detail", slug=review.game.slug)
    else:
        # otherwise show previous/old entires
        form = ReviewForm(instance=review)

    # returns data to template (form, review, game)
    return render(
        request,
        "games/review_form.html",
        {
            "form": form,
            "review": review,
            "game": review.game,
        },
    )


# only if you are logged in
@login_required
def review_delete(request, review_id):
    # review & id need to match & user logged in to be able to delte
    review = get_object_or_404(Review, id=review_id, user=request.user)
    game_slug = review.game.slug

    # delete only if it was submited
    if request.method == "POST":
        # remove reivew from records
        review.delete()
        # review erased confirmation for user
        messages.success(request, "Review was deleted successfully.")
        # return to main gamne page
        return redirect("game_detail", slug=game_slug)

    # failsafe
    return redirect("game_detail", slug=game_slug)


# can render games & games/category/<type>
def game_list(request, category_slug=None):
    query = request.GET.get("q", "").strip()
    # Katarina think it is better to have last games added displayed on top
    sort = request.GET.get("sort", "newest")
    get_category = request.GET.get("category", "").strip()
    # read games that in stock
    in_stock = request.GET.get("in_stock") == "1"

    # player filter
    players_min_raw = request.GET.get("players_min", "").strip()
    players_max_raw = request.GET.get("players_max", "").strip()

    def to_pos_int(value: str):
        try:
            n = int(value)
            return n if n > 0 else None
        except (TypeError, ValueError):
            return None

    players_min = to_pos_int(players_min_raw)
    players_max = to_pos_int(players_max_raw)

    players_exact_raw = request.GET.get("players_exact", "").strip()
    players_exact = to_pos_int(players_exact_raw)
    players_exact_only = request.GET.get("players_exact_only") == "1"

    # play time filter (minutes)
    time_min_raw = request.GET.get("time_min", "").strip()
    time_max_raw = request.GET.get("time_max", "").strip()

    time_min = to_pos_int(time_min_raw)
    time_max = to_pos_int(time_max_raw)

    # age filter (minimum age on the box, no max)
    age_min_raw = request.GET.get("age_min", "").strip()
    age_min = to_pos_int(age_min_raw)
    # for games that are age range unsorted (age restriction not set)
    age_include_unknown = request.GET.get("age_include_unknown") == "1"

    # If typed min time > max time - switch them 'bugfix'
    if time_min and time_max and time_min > time_max:
        time_min, time_max = time_max, time_min
        time_min_raw, time_max_raw = time_max_raw, time_min_raw

    # If typed min > max, swap (bugfix)
    if players_min and players_max and players_min > players_max:
        players_min, players_max = players_max, players_min
        players_min_raw, players_max_raw = players_max_raw, players_min_raw

    games = Game.objects.all()
    # rule for showing games in stock
    if in_stock:
        games = games.filter(stock__gt=0)

    # BUGFIX!!
    # If user used dropdown ?category=... on games, then
    # redirect to SEO URL /games/category/<type>
    # but now it should work on /games/
    # another BUGFIX - 'category' needs to be applied for real
    # redirect ONLY when category is actually selected /submited
    if "category" in request.GET:
        current_category = category_slug or ""

        if get_category != current_category:
            target_url = (
                reverse("game_list_by_category", args=[get_category])
                if get_category
                else reverse("game_list")  # user picked "All categories"
            )

            params = request.GET.copy()
            params.pop("category", None)
            params.pop("page", None)  # reset pagination when category changes
            qs = params.urlencode()

            return redirect(f"{target_url}?{qs}" if qs else target_url)

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

    # players filter
    if players_exact:
        if players_exact_only:
            # fixed player count only (if x=4 then 4–4)
            games = games.filter(
                min_players=players_exact,
                max_players=players_exact
            )
        else:
            # playable with X players (if X=5, then accept 2-6, 3-7)
            games = games.filter(
                min_players__lte=players_exact,
                max_players__gte=players_exact
            )

    else:
        # already existing logic (range OR single value as group size)
        if players_min and players_max:
            # show games whose player-range fully covers the users add range
            games = games.filter(
                min_players__lte=players_min,
                max_players__gte=players_max,
            )

        else:
            # if only min OR max is provided, tret as "group size"
            group_size_range = players_min or players_max
            if group_size_range:
                games = games.filter(
                    min_players__lte=group_size_range,
                    max_players__gte=group_size_range,
                )

    # min & max play time filter (minutes)
    if time_min and time_max:
        games = games.filter(
            min_play_time__gte=time_min, max_play_time__lte=time_max)
    elif time_min:
        games = games.filter(min_play_time__gte=time_min)
    elif time_max:
        games = games.filter(max_play_time__lte=time_max)

    # age filter (game min age <= player's age)
    if age_min:
        if age_include_unknown:
            games = games.filter(Q(age__lte=age_min) | Q(age__isnull=True))
        else:
            games = games.filter(age__lte=age_min)

    # sorting
    if sort == "price":
        games = games.order_by("price")
    elif sort == "-price":
        games = games.order_by("-price")
    elif sort == "newest":
        games = games.order_by("-created_at")
    elif sort == "oldest":
        games = games.order_by("created_at")
    # addinf descending order based on title (alphabet)
    elif sort == "-title":
        games = games.order_by("-title")
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

    # Sort UI helpers for title
    is_title_asc = sort == "title"
    is_title_desc = sort == "-title"

    # Clicking the price sort toggles direction
    price_toggle_sort = "-price" if is_price_asc else "price"

    # Clicck on title changes from A-z to Z-A
    title_toggle_sort = "-title" if is_title_asc else "title"

    # Click to place latest games on top or bottom
    is_newest = sort == "newest"
    is_oldest = sort == "oldest"
    newest_toggle_sort = "oldest" if is_newest else "newest"

    # base list url
    list_url = (
        reverse("game_list_by_category", args=[category_slug])
        if category_slug
        else reverse("game_list")
    )
    root_url = reverse("game_list")

    def build_qs(base_url, overrides=None, remove=None):
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
        return f"{base_url}?{qs}" if qs else base_url

    remove_search_url = build_qs(base_url=list_url, remove=["q"])
    remove_category_url = build_qs(base_url=root_url, remove=["category"])
    remove_in_stock_url = build_qs(base_url=list_url, remove=["in_stock"])
    # same rule (newst first) when fiters are discarded (Katarina's wish)
    remove_sort_url = build_qs(base_url=list_url, overrides={"sort": "newest"})
    clear_all_url = root_url
    remove_players_url = build_qs(
        base_url=list_url,
        remove=["players_min",
                "players_max",
                "players_exact",
                "players_exact_only"
                ]
    )
    remove_time_url = build_qs(
        base_url=list_url, remove=["time_min", "time_max"]
    )
    remove_age_url = build_qs(base_url=list_url,
                              remove=["age_min", "age_include_unknown"])

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
        # title sorting A-Z
        "is_title_asc": is_title_asc,
        # title storing Z-A
        "is_title_desc": is_title_desc,
        # reverts alphabet sorting to opposite of what it is currently
        "title_toggle_sort": title_toggle_sort,
        # last game adde on top
        "is_newest": is_newest,
        # last game added on bottom
        "is_oldest": is_oldest,
        # reset to opposite of what we have currently
        "newest_toggle_sort": newest_toggle_sort,
        # players filter values
        "players_min": players_min_raw,
        "players_max": players_max_raw,
        # remove link
        "remove_players_url": remove_players_url,
        # num value, but not ONLY that value
        "players_exact": players_exact_raw,
        # only x value, no diviations
        "players_exact_only": players_exact_only,
        # playtime filter min &max
        "time_min": time_min_raw,
        "time_max": time_max_raw,
        # remove play duration completly
        "remove_time_url": remove_time_url,
        # age value fitler
        "age_min": age_min_raw,
        # remove age filter
        "remove_age_url": remove_age_url,
        # undefinde / unexisting age restriction
        "age_include_unknown": age_include_unknown,
    }

    return render(request, "games/game_list.html", context)
