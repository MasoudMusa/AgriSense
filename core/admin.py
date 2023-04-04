from django.contrib import admin
from core.models import Message, Follower, Product

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# from .forms import CustomUserCreationForm
# from .models import User

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    model = User
    list_display = ('username', 'email', 'is_farmer', 'is_staff')


admin.site.register(User, CustomUserAdmin)
# Register your models here.
admin.site.register(Message)
admin.site.register(Follower)
# admin.site.register(Farmer)
admin.site.register(Product)
