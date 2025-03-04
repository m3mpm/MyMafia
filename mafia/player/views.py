from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're visited Mafia's main page.")
    # return render(request, 'player/index.html')


def players(request):
    return redirect('main')
    # return HttpResponse("List of all players")


def playerid(request, player_id):
    uri = reverse('players', args=(1,))
    return redirect(uri)
    # return HttpResponse(f"Player {player_id}")


def playerslug(request, player_name):
    if request.GET:
        print(request.GET)

    if not player_name:
        raise Http404()
    else:
        return HttpResponse(f"Player {player_name}")



def page_not_found(request, exception):
    # return render(request, '<h1>404.html</h1>')
    return HttpResponseNotFound("Sorry, we couldn't find that page.")