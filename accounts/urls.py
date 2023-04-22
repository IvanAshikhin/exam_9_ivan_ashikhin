from django.urls import path
from accounts.views import LoginView, RegisterView, ProfileView
from accounts.views import logout_view

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
