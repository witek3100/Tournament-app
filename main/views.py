from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response, "main/home.html", {})

def create_league(response):
    if response.method == "POST":
        form = (response.POST)
