from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User modelimiz için bir rest_framework ile ara katman olarak kullanabileceğimiz 
    bir serializer yaratıyoruz.
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

    def create(self, validated_data):
        # return super().create(validated_data)
        return User.objects.create(**validated_data)
