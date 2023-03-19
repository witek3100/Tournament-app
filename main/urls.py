from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createleague/', views.create_league, name='create league'),
    path('<int:id>', views.league, name='index'),
    path('<int:lid>/<int:tid>', views.team, name='player index')
]