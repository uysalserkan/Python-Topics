from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    """
    Burada standart bir kullanıcının modeilini oluşturacağız.
    """

    profile_pic = models.ImageField(null=True, default="def.jpeg", blank=True)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = "Customers"


class Tag(models.Model):
    """
        Productların uygun tagları alması için gerekli olan bir class.
    """
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = "Tags"


class Product(models.Model):
    """
        Bu kısımda ürünlerimizin genel özelliklerini belirteceğiz.
    """
    CATEGORIES = (
        ("In door", "In door"),
        ("Out door", "Out door"),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=20, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=400, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name

    class meta:
        verbose_name_plural = "Products"


class Order(models.Model):
    """
      Bu kısımda oluşturulan siparişlerin bilgileri tutulacaktır.
    """
    STATUS = (
        ("PENDING", "PENDING"),
        ("ON GOING", "ON GOING"),
        ("DELIVERED", "DELIVERED"),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS, max_length=200, null=True)

    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return str(self.customer.name + " || " + self.product.name)

    class meta:
        verbose_name_plural = "Orders"
