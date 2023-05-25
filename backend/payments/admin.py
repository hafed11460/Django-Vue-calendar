from django.contrib import admin
from payments.models import Subscription,Package,PackageFeature


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_id',
        'amount',
        'user',
        'duration',
        'package',
        'created_at',
        'start_date',
        'end_date',
        'success',
        'active',
        'is_paid',)

    def get_amount(self,obj):
        if obj.duration == Subscription.SIX_MONTHS:
            return obj.package.six_months_price

        if obj.duration == Subscription.ONE_YEAR:
            return obj.package.one_year_price

        if obj.duration == Subscription.TWO_YEARS:
            return obj.package.two_years_price
        return 0


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'currency',
        'package_type',
        'six_months_price',
        'one_year_price',
        'two_years_price', )

class PackageFeatureAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Subscription , SubscriptionAdmin)
admin.site.register(Package , PackageAdmin)
admin.site.register(PackageFeature , PackageFeatureAdmin)
