from django.shortcuts import render
from django.http import HttpResponse
from .models import League
from .forms import CreateLeagueForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def index(response, id):
    l = League.objects.get(league_id=id)
    if response.method == "POST":
        if response.POST.get("addTeam"):
            team_name = response.POST.get("team name")
            if len(team_name) <= 30:
                l.team_set.create(name=team_name, shorthand=team_name[:3])
        elif response.POST.get("deleteL"):
            League.objects.filter(league_id=id).delete()
            return redirect('/')

    return render(response, 'main/league.html', {"l" : l})

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

