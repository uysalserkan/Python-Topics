from django.db import models

# Create your models here.


class Makale(models.Model):
    yazar = models.CharField(max_length=150)
    baslik = models.CharField(max_length=150)
    aciklama = models.CharField(max_length=150)
    metin = models.TextField()
    sehir = models.CharField(max_length=150)
    yayim_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.baslik

    class Meta:
        verbose_name_plural = "Makaleler"
