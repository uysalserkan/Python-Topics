from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# API Viewlarını yaratıyoruz..


class RegisterView(APIView):
    """
    Bu View'ımızda bir kullanıcının post methodu ile kayıt olabilmesini sağlıyoruz.
    """

    def post(self, request):
        serialized = UserSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
        # if serialized.is_valid(raise_exception=True):
        #     serialized.save()
        #     return Response(serialized.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
