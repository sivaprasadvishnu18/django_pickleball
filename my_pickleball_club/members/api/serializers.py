from rest_framework import serializers

class MemberSerializer(serializers.Serializer):
    memberId = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()
    date_joined = serializers.CharField()
    active = serializers.BooleanField() 