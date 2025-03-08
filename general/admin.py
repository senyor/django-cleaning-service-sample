from django.contrib import admin

from general.models import TypesOfService, Order, UserProfile

# Register your models here.

admin.site.register(TypesOfService)
admin.site.register(Order)
admin.site.register(UserProfile)
