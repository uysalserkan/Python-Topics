# API url'leri bulunuyor (bir önceki alıştırmada api klasörünün içerisinde yapmıştık)..

from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
]
