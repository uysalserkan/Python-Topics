from rest_framework import serializers
from main.models import Makale

# DB üzerinden gelecek olan verileri python verilerine çevirip kolayca kullanabilme
# imkanı sunacak.


class MakaleSerializer(serializers.Serializer):
    """
    DB üzerinden gelebilecek tüm alanları işaretliyoruz.
    """

    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayim_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    güncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validate_data):
        """
        Bu fonksiyon ile yeni bir data oluşturabiliriz db üzerinde.
        """

        print(f"Validated DATA\n\n{validate_data}")
        return Makale.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """
        DB içerisinde bulunan bir objeyi değiştirmeye olanak sağlar.
        """

        instance.yazar = validated_data.get("yazar", instance.yazar)
        instance.baslik = validated_data.get("baslik", instance.baslik)
        instance.aciklama = validated_data.get("aciklama", instance.aciklama)
        instance.metin = validated_data.get("metin", instance.metin)
        instance.sehir = validated_data.get("sehir", instance.sehir)
        instance.yayim_tarihi = validated_data.get(
            "yayim_tarihi", instance.yayim_tarihi
        )
        instance.aktif = validated_data.get("aktif", instance.aktif)

        instance.save()
        return instance
