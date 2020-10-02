from django.urls import path
from .views import userSignup, activateAccount, UserProfile

urlpatterns = [
    path('signup/', userSignup, name='signup'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', activateAccount, name='activate'),
]