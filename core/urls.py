from django.urls import path

from . import views

urlpatterns = [
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/user/change-password/',
         views.change_password_view, name='change_password'),
    path('user/', views.user_detail_view, name='user_detail'),
    path('user/update/', views.UserUpdateView.as_view(), name='user_update'),
#     path('user/create/', views.create_user_view, name='create_user'),
    path('user/<int:pk>/', views.UserDetailView.as_view(),
         name='user_detail_by_id'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]
