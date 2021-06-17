from django.db import models

# Create your models here.


class Authors(models.Model):
    """
    Makaleleri yazan yazarların DB üzerinde bulunacak modelleri.
    """

    isim = models.CharField(max_length=120, null=False)
    soyisim = models.CharField(max_length=120, null=False)
    biyografi = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.isim}_{self.soyisim}"

    class Meta:
        verbose_name_plural = "Yazarlar"


class Makale(models.Model):
    yazar = models.ForeignKey(
        Authors, on_delete=models.CASCADE, related_name="makaleler"
    )
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
