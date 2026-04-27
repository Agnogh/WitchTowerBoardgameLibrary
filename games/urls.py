from django.urls import path
from . import views

urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("categories/", views.category_counts_page, name="category_counts"),
    path("category/<slug:category_slug>/",
         views.game_list, name="game_list_by_category"),
    path("contact/", views.contact_page, name="contact_page"),
    path("events/", views.events_page, name="events_page"),
    path("reviews/<int:review_id>/edit/", views.review_edit,
         name="review_edit"),
    path("reviews/<int:review_id>/delete/", views.review_delete,
         name="review_delete"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),

]
