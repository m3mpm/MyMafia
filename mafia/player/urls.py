from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('players/', views.players, name='players'),
    path('players/<int:player_id>/', views.playerid, name='player'),
    path('players/<slug:player_name>/', views.playerslug, name='player_name'),
]
