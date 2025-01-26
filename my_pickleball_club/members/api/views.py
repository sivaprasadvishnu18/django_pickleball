from uuid import UUID
from django.http import JsonResponse
from members.models import Member, Team, Tournament, Tournament_Win
from members.api.serializers import MemberSerializer, TeamSerializer, TournamentSerializer, TournamentWinsSerializer
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class membersListAV(APIView):
    def get(self, request):
        mymembers = Member.objects.all()
        serializer = MemberSerializer(mymembers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if(request.data):
            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
            
class memberByIdAV(APIView):
    def get(self, request, id):
        try:
            mymember = Member.objects.get(memberId=id)
        except Member.DoesNotExist:
            return Response({'Error': 'No member by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MemberSerializer(mymember, many=False) 
        return Response(serializer.data)
    
    def put(self, request, id):
        mymember = Member.objects.get(memberId=id)
        serializer = MemberSerializer(instance = mymember, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        mymember = Member.objects.get(memberId=id)
        mymember.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class teamsListAV(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if(request.data):
            serializer = TeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
            
class teamByIdAV(APIView):
    def get(self, request, id):
        try:
            team = Team.objects.get(teamId=id)
        except Team.DoesNotExist:
            return Response({'Error': 'No team by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(team) 
        return Response(serializer.data)
    
    def put(self, request, id):
        team = Team.objects.get(teamId=id)
        serializer = TeamSerializer(instance = team, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        team = Team.objects.get(teamId=id)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class tournamentWinsListAV(APIView):
    def get(self, request):
        tournament_wins = Tournament_Win.objects.all()
        serializer = TournamentWinsSerializer(tournament_wins, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if(request.data):
            serializer = TournamentWinsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
            
class tournamentWinsByIdAV(APIView):
    def get(self, request, id):
        try:
            tournament_win = Tournament_Win.objects.get(id=id)
        except Tournament_Win.DoesNotExist:
            return Response({'Error': 'No tournament win by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TournamentWinsSerializer(tournament_win) 
        return Response(serializer.data)
    
    def put(self, request, id):
        tournament_win = Tournament_Win.objects.get(id=id)
        serializer = TournamentWinsSerializer(instance = tournament_win, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        tournament_win = Tournament_Win.objects.get(id=id)
        tournament_win.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class tournamentsListAV(APIView):
    def get(self, request):
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if(request.data):
            serializer = TournamentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)

class tournamentByIdAV(APIView):
    def get(self, request, id):
        try:
            tournament = Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
            return Response({'Error': 'No tournament by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TournamentSerializer(tournament) 
        return Response(serializer.data)
    
    def put(self, request, id):
        tournament = Tournament.objects.get(tournamentId=id)
        serializer = TournamentSerializer(instance = tournament, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        tournament = Tournament.objects.get(tournamentId=id)
        tournament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Function based views
# @api_view(['GET', 'POST'])
# def members(request):
#     if request.method == 'GET':
#         mymembers = Member.objects.all()
#         serializer = MemberSerializer(mymembers, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         if(request.data):
#             serializer = MemberSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             else:
#                 return Response(serializer.errors, status=400)
  
# @api_view(['GET', 'PUT', 'DELETE'])
# def memberById(request, id):
#     if request.method == 'GET':
#         try:
#             mymember = Member.objects.get(memberId=id)
#         except Member.DoesNotExist:
#             return Response({'Error': 'No member by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MemberSerializer(mymember, many=False) 
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         mymember = Member.objects.get(memberId=id)
#         serializer = MemberSerializer(instance = mymember, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         mymember = Member.objects.get(memberId=id)
#         mymember.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'POST'])
# def teams(request):
#     if request.method  == 'GET':
#         teams = Team.objects.all()
#         serializer = TeamSerializer(teams, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         if(request.data):
#             serializer = TeamSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             else:
#                 return Response(serializer.error, status=400)
            
# @api_view(['GET', 'PUT', 'DELETE'])
# def teamById(request, id):
#     if request.method == 'GET':
#         try:
#             team = Team.objects.get(teamId=id)
#         except Team.DoesNotExist:
#             return Response({'Error': 'No team by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = TeamSerializer(team) 
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         team = Team.objects.get(teamId=id)
#         serializer = TeamSerializer(instance = team, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         team = Team.objects.get(teamId=id)
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)