from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class TypesOfService(models.Model):
    name = models.CharField(verbose_name='Наименование типа сервиса', max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('0', "Наличные"),
        ('1', "Банковская карта")
    ]
    STATUS_CHOICES = [
        ('0', "Новая"),
        ('1', "В работе"),
        ('2', "Выполнено"),
        ('3', "Отменено")
    ]
    address = models.CharField(verbose_name='Адрес', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    date_at = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(TypesOfService, verbose_name='Тип услуги', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание иной услуги', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий при отмене заявки', null=True, blank=True)
    payment_type = models.CharField(
        max_length=1,
        choices=PAYMENT_TYPE_CHOICES,
        verbose_name='Тип оплаты'
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='0',
        verbose_name='Статус заявки'
    )
