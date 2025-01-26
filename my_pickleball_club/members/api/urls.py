from django.urls import path
from . import views

urlpatterns = [
    #Class based views
    path('members/', views.membersListAV.as_view(), name='members'),
    path('members/details/<uuid:id>/', views.memberByIdAV.as_view(), name='memberById'),
    
    #Function based views
    # path('members/', views.members, name='members'),
    # path('members/details/<uuid:id>/', views.memberById, name='memberById'),
    
    #Class based views
    path('teams/', views.teamsListAV.as_view(), name='teams'),
    path('teams/details/<uuid:id>/', views.teamByIdAV.as_view(), name='teamById'),
    
    #Function based views
    #path('teams/', views.teams, name='teams'),
    #path('teams/details/<uuid:id>/', views.teamById, name='teamById'),
    
    path('tournaments/', views.tournamentsListAV.as_view(), name='tournaments'),
    path('tournaments/details/<int:id>/', views.tournamentByIdAV.as_view(), name='tournamentById'),
    
    path('tournament-wins/', views.tournamentWinsListAV.as_view(), name='tournament_wins'),
    path('tournament-wins/details/<int:id>/', views.tournamentWinsByIdAV.as_view(), name='tournamentById'),
]