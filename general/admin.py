from django.contrib import admin

from general.models import TypesOfService, Order

# Register your models here.

admin.site.register(TypesOfService)
admin.site.register(Order)
