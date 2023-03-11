from django.shortcuts import render, redirect
from users.forms import SignUpForm
def login(response):
    return render(response, "users/login.html", {})

def signup(response):
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = SignUpForm()
    return render(response, "users/signup.html", {"form":form})
