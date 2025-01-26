from rest_framework import serializers
from members.models import Member, Team, Tournament_Win, Tournament

class TournamentSerializer(serializers.ModelSerializer):
    
    class Meta: 
        tournament = serializers.PrimaryKeyRelatedField(queryset=Tournament.objects.all())
        
        model = Tournament
        fields = "__all__"

class TournamentWinsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        wins = serializers.PrimaryKeyRelatedField(queryset=Tournament_Win.objects.all())
        
        model = Tournament_Win
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    tournament_wins = TournamentWinsSerializer(many=True, read_only = True)
    
    class Meta:
        tournament_wins = serializers.PrimaryKeyRelatedField(queryset=Tournament_Win.objects.all())
        
        model = Team
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    
    class Meta: 
        team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
        
        model = Member
        fields = "__all__"
        # You can also define the fields you want to serialize like this: fields = ['id, 'name', 'email']
        
        #You can add validations to the serializer by creating a method called validate_<field_name>
        
    #Old version of the serializer
    # memberId = serializers.UUIDField(read_only=True)
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # email = serializers.CharField()
    # phone = serializers.CharField()
    # date_joined = serializers.CharField()
    # active = serializers.BooleanField() 
    
    # def create(self, validated_data):
    #     return Member.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.memberId = validated_data.get('memberId', instance.memberId)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.date_joined = validated_data.get('date_joined', instance.date_joined)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
# class TournamentsWonSerializer(serializers.Serializer):
    
#     # class Meta: 
#     #     team = serializers.PrimaryKeyRelatedField(queryset=TournamentsWon.objects.all())
        
#     #     model = Member
#     #     fields = "__all__"
    
#     name = serializers.CharField(null=True)
#     count = serializers.DateField(null=True)
#     most_recent_win = serializers.CharField(null=True)
#     last_qualified = serializers.CharField(null=True)
#     teams = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='tournaments_won')
    
#     def create(self, validated_data):
#         return validated_data
    
#     def update(self, instance, validated_data):
#         instance.tournament_name = validated_data.get('tournament_name', instance.tournament_name)
#         instance.tournament_date = validated_data.get('tournament_date', instance.tournament_date)
#         instance.tournament_location = validated_data.get('tournament_location', instance.tournament_location)
#         instance.save()
#         return instance