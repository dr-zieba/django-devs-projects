from django.urls import path
from .views import profiles, userProfile, loginUser, logoutUser, registerUser


urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<str:pk>', userProfile, name='user-profile'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register')
]