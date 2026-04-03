from django.urls import path

from . import views

app_name = "players"

urlpatterns = [
    path("", views.player_list, name="list"),
    path("player/add/", views.player_create, name="create"),
    path("player/<int:player_id>/", views.player_detail, name="detail"),
    path("player/<int:player_id>/edit/", views.player_update, name="update"),
    path("player/<int:player_id>/delete/", views.player_delete, name="delete"),
]
