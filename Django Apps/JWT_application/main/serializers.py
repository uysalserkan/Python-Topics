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

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # return super().create(validated_data)
        usr_pass = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if usr_pass is not None:
            # burada kullanıcımızın şifresini django şifreleme fonksiyonu ile şifreliyoruz
            # direkt olarak database'de gözükmüyor..
            instance.set_password(usr_pass)

        instance.save()
        return instance
