from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from player.models import Player

# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string('player/index.html')
    # return HttpResponse(t)
    # return HttpResponse("Hello, world. You're visited Mafia's main page.")
    data = {'title': 'Main page', 'menu': menu, 'float': 28.56,
            'lst': [1, 2, 'abd', True], 'set': {1, 2, 3, 2, 5}, 'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10, 20)}
    return render(request, 'player/index.html', context=data)


def about(request):
    data = {'title': 'About page'}
    return render(request, 'player/about.html', {'title': 'About', 'menu': menu})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизоваться")


def show_players(request):
    # return HttpResponse("List of all players")
    return redirect('main')


def show_player_by_id(request, player_id):
    # uri = reverse('players', args=(1,))
    # return redirect(uri)
    # return HttpResponse(f"Player {player_id}")
    player = get_object_or_404(Player, pk=player_id)
    player_data = {'title': f'{player.first_name} {player.last_name}',
                   'data': {
                       'first_name': player.first_name,
                       'last_name': player.last_name,
                       'email': player.email,
                       'phone': player.phone,
                       'nickname': player.nickname,
                       'rating': player.rating,
                       'role': player.role,
                       'club': player.club,
                       }
                   }
    return render(request, 'player/show_players.html', context=player_data)


def show_player_by_slug(request, player_slug):
    player = get_object_or_404(Player, slug=player_slug)
    player_data = {'title': f'{player.first_name} {player.last_name}',
                   'data': {
                       'first_name': player.first_name,
                       'last_name': player.last_name,
                       'email': player.email,
                       'phone': player.phone,
                       'nickname': player.nickname,
                       'rating': player.rating,
                       'role': player.role,
                       'club': player.club,
                   }
                   }
    return render(request, 'player/show_players.html', context=player_data)

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

