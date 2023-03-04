from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response, "main/home.html", {})

def login(response):
    return render(response, "main/login.html", {})

def signup(response):
    return render(response, "main/signup.html", {})