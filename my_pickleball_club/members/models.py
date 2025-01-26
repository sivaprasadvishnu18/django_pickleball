import uuid
from django.db import models

# Create your models here.
class Member(models.Model):
    memberId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='members')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Team(models.Model):
    teamId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    team_name = models.CharField(max_length=100)
    team_joined = models.DateField(max_length=100)
    
    def __str__(self):
        return f'{self.team_name}'
    
class Tournament_Win(models.Model):
    
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, null=True, related_name='tournament_wins')
    number_of_wins = models.IntegerField(null=True)
    most_recent_win = models.CharField(null=True, max_length=100)
    last_qualified = models.CharField(null=True, max_length=50)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='tournament_wins')
    
    def __str__(self):
        return f'{self.tournament}'
    
    
class Tournament(models.Model):
    
    name = models.CharField(null=True, max_length=50)
    number_of_teams = models.IntegerField(null=True)
    country = models.CharField(null=True, max_length=50)
    
    def __str__(self):
        return f'{self.name}'
    
