from .models import Product
from .models import Product
from rest_framework import serializers, viewsets
from .models import Follower
from .models import Message
from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_farmer', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']


class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follower
        fields = ('id', 'follower', 'following', 'created_at')


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'quantity', 'price', 'location')


# class FarmerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farmer
#         fields = ('id', 'name', 'email', 'phone_number', 'location')


class ProductSerializer(serializers.ModelSerializer):
    farmer = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'quantity',
                  'price', 'location', 'farmer')

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'is_farmer')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
