from django.urls import path, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/register/', views.UserRegistrationView.as_view(), name='register'),
    path('auth/user/change-password/',
         views.change_password_view, name='change_password'),
    path('user/', views.user_detail_view, name='user_detail'),
    path('user/update/', views.UserUpdateView.as_view(), name='user_update'),
    # path('user/create/', views.create_user_view, name='create_user'),
    path('user/<int:pk>/', views.UserDetailView.as_view(),
         name='user_detail_by_id'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    #
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/create/<str:username>/',
         views.MessageCreateView.as_view(), name='create-message'),
    path('follow/<str:username>/', views.FollowUser.as_view(), name='follow-user'),
    path('unfollow/<str:username>/',
         views.UnfollowUser.as_view(), name='unfollow-user'),

]
