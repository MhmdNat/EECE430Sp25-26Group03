from django.db import DatabaseError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VoleyPlayerForm
from .models import VoleyPlayer


def player_list(request):
    players = VoleyPlayer.objects.all().order_by("id")
    return render(request, "players/list.html", {"players": players})


def player_detail(request, player_id):
    player = get_object_or_404(VoleyPlayer, pk=player_id)
    return render(request, "players/detail.html", {"player": player})


def player_create(request):
    db_error = None

    if request.method == "POST":
        form = VoleyPlayerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("players:list")
            except DatabaseError:
                db_error = "Could not save player. Please try again."
    else:
        form = VoleyPlayerForm()

    context = {
        "form": form,
        "title": "Add Player",
        "db_error": db_error,
    }
    return render(request, "players/form.html", context)


def player_update(request, player_id):
    player = get_object_or_404(VoleyPlayer, pk=player_id)
    db_error = None

    if request.method == "POST":
        form = VoleyPlayerForm(request.POST, instance=player)
        if form.is_valid():
            try:
                form.save()
                return redirect("players:detail", player_id=player.id)
            except DatabaseError:
                db_error = "Could not update player. Please try again."
    else:
        form = VoleyPlayerForm(instance=player)

    context = {
        "form": form,
        "title": "Edit Player",
        "player": player,
        "db_error": db_error,
    }
    return render(request, "players/form.html", context)


def player_delete(request, player_id):
    player = get_object_or_404(VoleyPlayer, pk=player_id)
    db_error = None

    if request.method == "POST":
        try:
            player.delete()
            return redirect("players:list")
        except DatabaseError:
            db_error = "Could not delete player. Please try again."

    return render(
        request,
        "players/confirm_delete.html",
        {"player": player, "db_error": db_error},
    )
