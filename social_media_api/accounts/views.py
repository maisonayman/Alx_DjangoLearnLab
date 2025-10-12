from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User
# Create your views here.

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=400)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if request.user == target_user:
        return Response({'error': "You cannot follow yourself."}, status=400)
    
    request.user.following.add(target_user)
    return Response({'message': f'You are now following {target_user.username}.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if target_user in request.user.following.all():
        request.user.following.remove(target_user)
        return Response({'message': f'You unfollowed {target_user.username}.'})
    return Response({'error': 'You are not following this user.'}, status=400)



