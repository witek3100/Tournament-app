from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createleague/', views.create_league, name='create league'),
    path('<int:id>', views.index, name='index')
]