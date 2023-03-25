from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="league", null=True)
    league_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    promoted_teams = models.IntegerField(default=1)
    relegated_teams = models.IntegerField(default=1)

class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    shorthand = models.CharField(max_length=3)
    points = models.IntegerField(null=False, default=0)
    goals_scored = models.IntegerField(null=False, default=0)
    goals_lost = models.IntegerField(null=False, default=0)
    wins = models.IntegerField(null=False, default=0)
    draws = models.IntegerField(null=False, default=0)
    lost = models.IntegerField(null=False, default=0)

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)

class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_day = models.IntegerField()
    home_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="hometeam")
    away_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="awayteam")
    home_team_result = models.IntegerField(null=True)
    away_team_result = models.IntegerField(null=True)