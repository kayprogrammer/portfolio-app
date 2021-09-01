from django.db import models
# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Suscriber(models.Model):
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.email