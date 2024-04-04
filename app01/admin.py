from django.contrib import admin
from .models import Products,Product,CartItem,Cart
from .models import Profile

admin.site.register(Profile)
# Register your models here.

admin.site.register(Products)
admin.site.register(Product)

admin.site.register(CartItem)
admin.site.register(Cart)

