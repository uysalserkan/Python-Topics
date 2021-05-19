from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, null=False,)
    desc = models.TextField(max_length=400, null=True, blank=True,)
    complete = models.BooleanField(default=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tasks"
