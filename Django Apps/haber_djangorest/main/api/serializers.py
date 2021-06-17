from rest_framework import serializers
from main.models import Authors, Makale

from django.utils.timesince import timesince
from datetime import date, datetime, timezone

# DB üzerinden gelecek olan verileri python verilerine çevirip kolayca kullanabilme
# imkanı sunacak.


class MakaleSerializer(serializers.ModelSerializer):
    """
    ModelSerializer ile daha kolay ve hızlı bir biçimde serializer'ımızı oluşturabiliriz.
    """

    # JSON verimiz içerisinde yazarların bilgilerini bastırıyoruz.

    # yazar = (
    #     AuthorSerializer()
    # )

    time_pub = (
        serializers.SerializerMethodField()
    )  # Yaratılma tarihini DB üzerinden gelmeden buradan çıkarım yaparak yeni bir attribute oluşturup gösterebiliriz.

    class Meta:
        """
        Formlar gibi hangi alanları kullanacaz hangilerini kullanmayacağımızı belirtebilriz bu class içerisinde.
        """

        model = Makale
        fields = "__all__"
        read_only_fields = ["id", "yaratilma_tarihi", "güncellenme_tarihi"]

    def get_time_pub(self, object):
        """
        Object Validation.
        Yaratılma tarihinin üzerinden ne kadar zaman geçtiğini hesaplayıp json içerisinde
        yeni bir attribute olarak gösterebildiğimiz fonksiyon.
        """
        now_date = datetime.now(timezone.utc)
        if object.aktif:
            pub_date = object.yaratilma_tarihi

            return timesince(pub_date, now_date)
        else:
            return "Makale aktif değil, lütfen ilk önce makaleyi aktif ediniz."

    def validate_yayim_tarihi(self, pub_date):
        """
        Field Validation.
        Ileri bir yayımlanma tarihini engelliyoruz.
        """
        if pub_date > date.today():
            raise serializers.ValidationError(
                "Yayımlanma tarihi ileri bir tarih olamaz."
            )
        return pub_date


class AuthorSerializer(serializers.ModelSerializer):
    """
    Yazarlarımızı bu serializer ile hızlı bir şekilde listeleyebilir ve gösterebiliriz.
    """

    # makaleler adında yeni bir alan oluşturuyoruz ve bu alanda yazarlarımızın makalelerini gösteriyoruz.
    # makaleler = MakaleSerializer(many=True, read_only=True)
    # burada ise makalelerin linkini gösteriyoruz..
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="makale-detail",  # burada girdiğimiz view_name url de bulunan name'dir ve linkleme işlemi gerçekleştirecektir..
        lookup_field="id",  # bu alan ile her bir id ile oluşturulan makaleleri linkliyoruz. Bu olmadan hata veriyor..
    )

    class Meta:
        model = Authors
        fields = "__all__"


class oldMakaleSerializer(serializers.Serializer):
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

    def validate(self, data):
        """
        object seviyesinde kontrol yapıyoruz.
        Tüm data üzerinde kontrol işlemlerini gerçekleştiriyoruz.
        """
        if data["baslik"] == data["aciklama"]:
            raise serializers.ValidationError(
                "Baslik ve açıklama aynı olamaz. Lütfen kontrol edip tekrar giriniz.."
            )

    def validate_baslik(self, value):
        """
        field seviyesinde kotrol işlemi gerçekleştiriyoruz.
        """
        if len(value) < 15:
            raise serializers.ValidationError(
                f"Baslik için en az 25 karakter girmeniz gerekiyor. ({25-len(value)} karakter daha girmelisiniz)"
            )
        return value
