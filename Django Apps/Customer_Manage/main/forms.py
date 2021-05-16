from django.forms import ModelForm
from .models import Customer, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Order class'ında bulunan tüm attributelere field aç demek
        # bunu yerine ['name', ..] gibi de yazabilirdik.


class CreateUserForm(UserCreationForm):
    """ Kullanıcı kayıt olurken oluşturulan ekran"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    """ Burada user profile picture için ayarlamalar yapılıyor."""
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
