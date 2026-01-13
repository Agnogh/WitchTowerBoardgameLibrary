from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.game_detail, name="game_detail"),
]
