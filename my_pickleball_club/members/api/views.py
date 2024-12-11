from django.http import JsonResponse
from members.models import Member, Team
from members.api.serializers import MemberSerializer, TeamSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def members(request):
    if request.method == 'GET':
        mymembers = Member.objects.all()
        serializer = MemberSerializer(mymembers, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        if(request.data):
            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
  
@api_view(['GET', 'PUT', 'DELETE'])
def memberById(request, id):
    if request.method == 'GET':
        mymember = Member.objects.get(memberId=id)
        serializer = MemberSerializer(mymember, many=False) 
        return Response(serializer.data)
    
    if request.method == 'PUT':
        mymember = Member.objects.get(memberId=id)
        serializer = MemberSerializer(instance = mymember, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    if request.method == 'Delete':
        mymember = Member.objects.get(memberId=id)
        mymember.delete()
        return Response()
    
@api_view(['GET', 'POST'])
def teams(request):
    if request.method  == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if(request.data):
            serializer = TeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.error, status=400)
            
@api_view(['GET', 'PUT', 'DELETE'])
def teamById(request, id):
    if request.method == 'GET':
        try:
            team = Team.objects.get(teamId=id)
        except Team.DoesNotExist:
            return Response({'Error': 'No team by that ID exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(team) 
        return Response(serializer.data)
    
    if request.method == 'PUT':
        team = Team.objects.get(teamId=id)
        serializer = TeamSerializer(instance = team, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    if request.method == 'Delete':
        team = Team.objects.get(teamId=id)
        team.delete()
        return Response()