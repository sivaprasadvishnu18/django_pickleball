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
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Team(models.Model):
    teamId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    team_name = models.CharField(max_length=100)
    team_joined = models.DateField(max_length=100)
    
