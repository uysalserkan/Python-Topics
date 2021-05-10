from django.db import models

# Create your models here.


class Customer(models.Model):
    """
    Burada standart bir kullanıcının modeilini oluşturacağız.
    """

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = "Customers"


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
    description = models.CharField(max_length=400, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

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

    def __str__(self) -> str:
        return self.date_created

    class meta:
        verbose_name_plural = "Orders"

