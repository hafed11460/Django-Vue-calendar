from django.contrib import admin
from .models import Product
from .models import Package , PackageFeature
# Register your models here.

class PackageFeatureAdmin(admin.ModelAdmin):
    list_display = ['title']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name','monthly_price','annual_price']

admin.site.register(PackageFeature,PackageFeatureAdmin)
admin.site.register(Package,PackageAdmin)
# admin.site.register(Product)