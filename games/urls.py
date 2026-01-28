from django.urls import path
from . import views

urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("category/<slug:category_slug>/",
         views.game_list, name="game_list_by_category"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),
]
