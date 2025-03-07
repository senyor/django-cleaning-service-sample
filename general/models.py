from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class TypesOfService(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('0', "Наличные"),
        ('1', "Банковская карта")
    ]
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    date_at = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(TypesOfService, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    payment_type = models.CharField(
        max_length=1,
        choices=PAYMENT_TYPE_CHOICES
    )
