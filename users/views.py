from django.shortcuts import render

def login(response):
    return render(response, "users/login.html", {})

def signup(response):
    return render(response, "users/signup.html", {})
