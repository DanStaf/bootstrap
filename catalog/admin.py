from django.contrib import admin

from catalog.models import Product, Category, Contact, Version

# Register your models here.

"""
user: postgres
password: admin
"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'version_is_active')
