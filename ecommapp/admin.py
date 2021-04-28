from django.contrib import admin
from ecommapp.models import Product
from .models import Contact, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
