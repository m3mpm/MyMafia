from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're visited Mafia's main page.")
    # return render(request, 'player/index.html')


def page_not_found(request, exception):
    # return render(request, '<h1>404.html</h1>')
    return HttpResponseNotFound("Sorry, we couldn't find that page.")


def players(request):
    return HttpResponse("List of all players")


def playerid(request, player_id):
    return HttpResponse(f"Player {player_id}")


def playerslug(request, player_name):
    return HttpResponse(f"Player {player_name}")