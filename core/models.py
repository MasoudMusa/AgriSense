# models.py

from django.utils.timezone import now
import datetime
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)

    class Meta:
        app_label = 'core'


class Message(models.Model):
    sender = models.ForeignKey(
        'core.CustomUser', related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        'core.CustomUser', related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.sender).capitalize()} message to {str(self.recipient).capitalize()}'


class Follower(models.Model):
    follower = models.ForeignKey(
        'core.CustomUser', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(
        'core.CustomUser', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.follower} -> {self.following}'

    @staticmethod
    def get_connections(user):
        return user.following.all()


# class Farmer(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Product(models.Model):
    farmer = models.ForeignKey(
        'core.CustomUser', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} posted by {str(self.farmer.username).capitalize()}'
