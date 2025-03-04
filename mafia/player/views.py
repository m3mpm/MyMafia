from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

menu = ["О сайте", "Игроки", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    data = {'title': 'Main page', 'menu': menu, 'float': 28.56,
            'lst': [1, 2, 'abd', True], 'set': {1, 2, 3, 2, 5}, 'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10, 20)}
    return render(request, 'player/index.html', context=data)
    # t = render_to_string('player/index.html')
    # return HttpResponse(t)
    # return HttpResponse("Hello, world. You're visited Mafia's main page.")


def about(request):
    data = {'title': 'About page'}
    return render(request, 'player/about.html', data)


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
