from rest_framework import serializers
from members.models import Member, Team

class MemberSerializer(serializers.Serializer):
    memberId = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()
    date_joined = serializers.CharField()
    active = serializers.BooleanField() 
    
    def create(self, validated_data):
        return Member.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.memberId = validated_data.get('memberId', instance.memberId)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
class TeamSerializer(serializers.Serializer):
    teamId = serializers.UUIDField(read_only=True)
    team_joined = serializers.CharField()
    team_name = serializers.CharField()
    
    
    def create(self, validated_data):
        return Team.objects.create(**validated_data)