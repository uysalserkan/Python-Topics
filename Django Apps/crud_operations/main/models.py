from django.db import models


class Positions(models.Model):
    """
        Kullanıcıların pozisyonları hakkında biligileri içeren model
    """

    title = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.title


class Employee(models.Model):
    """
        Kullanıcıların bilgilerini içeren sınıf
    """
    fullname = models.CharField(max_length=80, null=False)
    emp_code = models.CharField(max_length=3, null=False)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.fullname
