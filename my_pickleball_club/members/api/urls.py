from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<uuid:id>/', views.memberById, name='memberById'),
    
    path('teams/', views.teams, name='teams'),
    path('teams/details/<uuid:id>/', views.teamById, name='teamById'),
]