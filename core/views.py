from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from .serializers import FollowerSerializer, UserSerializer
from .models import Follower
from .models import Message, Follower
from .serializers import MessageSerializer
from .models import Message
from rest_framework import permissions
from rest_framework import generics
import re

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from core.helpers import valid_email_address
from . import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    """
    Login a user with email and password.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def logout_view(request):
    """
    Logout a user.
    """
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_view(request):
    """
    Register a new user with email and password.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    # Validate email
    if not email:
        return Response({'error': 'Email address is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not valid_email_address(email):
        return Response({'error': 'Invalid email address'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email address already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Validate password
    try:
        validate_password(password)
    except ValidationError as e:
        return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    # Create user
    user = User.objects.create_user(email, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'success': 'User created successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_detail_view(request):
    """
    Get details of the current authenticated user.
    """
    user = request.user
    return Response({
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def change_password_view(request):
    """
    Change the password of the current authenticated user.
    """
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    if not user.check_password(old_password):
        return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        validate_password(new_password)
    except ValidationError as e:
        return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
    user.set_password(new_password)
    user.save()
    return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


class UserDetailView(generics.RetrieveAPIView):
    """
    Get the details of a specific user by ID.
    """
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id)


class UserUpdateView(generics.UpdateAPIView):
    """
    Update the details of the current authenticated user.
    """
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # TODO user can send message to self
        sender = self.request.user
        recipient = User.objects.get(username=self.kwargs['username'])
        serializer.save(sender=sender, recipient=recipient)


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # connections = Follower.get_connections(user)
        # TODO is this to get incoming or outgoung messages?
        return Message.objects.filter(recipient=user)


class FollowUser(generics.CreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, username):
        user_to_follow = User.objects.get(username=username)

        # Check if the user is already following the user_to_follow
        if Follower.objects.filter(follower=request.user, following=user_to_follow).exists():
            return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)

        follower = Follower(follower=request.user, following=user_to_follow)
        follower.save()

        return Response(FollowerSerializer(follower).data, status=status.HTTP_201_CREATED)


class UnfollowUser(generics.DestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, username):
        user_to_unfollow = User.objects.get(username=username)
        follower = Follower.objects.filter(
            follower=request.user, following=user_to_unfollow)

        if not follower.exists():
            return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)

        follower.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FarmerViewSet(viewsets.ModelViewSet):
    # TODO Is every user a farmer? and can user access all farmers.
    queryset = User.objects.filter(is_farmer=True)
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
