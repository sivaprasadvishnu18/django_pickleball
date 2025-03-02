from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'],)
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    
    if request.user.is_authenticated:
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "registration Successfull!"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            print("hello" ,token)
            
        else:
            data = serializer.errors
            
        return Response(data)