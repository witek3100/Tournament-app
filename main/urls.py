from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createleague/', views.create_league, name='create league'),
    path('<int:id>', views.league, name='index'),
    path('<int:lid>/<int:tid>', views.team, name='player index'),
    path('<int:lid>/editmatch/<int:mid>', views.edit_match, name='edit match'),
    path('<int:lid>/createteam/', views.create_team, name='create team'),
    path('<int:lid>/<int:tid>/addplayer', views.create_player, name='player index'),
]