from django.contrib import admin
from .models import Product


# Register your models here
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'slug', 'created_at', 'updated_at', 'active')
