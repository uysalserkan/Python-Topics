from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from .models import User
# Create your views here.

# API Viewlarını yaratıyoruz..


class RegisterView(APIView):
    """
    Bu View'ımızda bir kullanıcının post methodu ile kayıt olabilmesini sağlıyoruz.
    """

    def post(self, request):
        serialized = UserSerializer(data=request.data)

        # serialized.is_valid(raise_exception=True)
        # serialized.save()
        # return Response(serialized.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Kullanıcı girişi yapabileceğimiz sınıf.
    """

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed(
                "User not found. Please try to register..")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed(
                "Your password is incorrect. Please check and try again..")

        return Response({
            'message': 'Successfully logged in.'
        })
