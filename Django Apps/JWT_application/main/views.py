from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import datetime
from .models import User
import jwt
from .secrets import SECRETS
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

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            # 60 dakika boyunca token aktif olacak daha sonra pasif hale gelecektir.

            'iat': datetime.datetime.utcnow()
            # Token'in oluşturulma zamanı
        }

        token = jwt.encode(
            payload=payload,
            key=SECRETS['JWT_SECRET_KEY'],
            algorithm='HS256'
        )

        resp = Response()

        # httponly front end token i görememesi için.
        resp.set_cookie(key='jwt', value=token, httponly=True)

        resp.data = {
            'token': token
        }

        return resp
