# API url'leri bulunuyor (bir önceki alıştırmada api klasörünün içerisinde yapmıştık)..

from django.urls import path
from .views import LoginView, LogoutView, RegisterView, UserView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user', UserView.as_view(), name='user'),
]
