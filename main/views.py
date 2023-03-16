from django.shortcuts import render
from django.http import HttpResponse
from .models import League
from .forms import CreateLeagueForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
def home(response):
    return render(response, "main/home.html", {})

@login_required
def create_league(request):
    if request.method == "POST":
        form = CreateLeagueForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/')
    else:
        form = CreateLeagueForm()
    return render(request, 'main/create_league.html', {'form':form})