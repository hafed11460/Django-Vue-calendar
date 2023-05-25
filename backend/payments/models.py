from django.db import models
from django.contrib.auth.models import User
from products.models import Package
import datetime
from django.utils import timezone

class PackageFeature(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Package(models.Model):
    EGP = 'EGP'
    CURRENCIES = (
        (EGP,'EGP'),
    )

    SILVER  = 'S'
    GOLD    = 'G'
    DIAMOND = 'D'
    PAKAGE_TYPE = (
        (GOLD,'Gold'),
        (SILVER,'Silver'),
        (DIAMOND,'Diamond'),
    )
    title = models.CharField(max_length=100, unique=True)
    package_type = models.CharField(choices=PAKAGE_TYPE,max_length=10)
    six_months_price = models.DecimalField(default=10, decimal_places=2, max_digits=6)
    one_year_price = models.DecimalField(default=10, decimal_places=2, max_digits=6)
    two_years_price = models.DecimalField(default=10, decimal_places=2, max_digits=6)
    currency = models.CharField(choices=CURRENCIES,default=EGP, max_length=50)
    description = models.TextField(verbose_name="Description")
    features  = models.ManyToManyField("PackageFeature")

    def __str__(self):
        return self.title


class Subscription(models.Model):
    SIX_MONTHS = '1'
    ONE_YEAR   = '2'
    TWO_YEARS  = '3'
    DURATION_TYPE = (
        (SIX_MONTHS,'6 Months'),
        (ONE_YEAR,'1 year'),
        (TWO_YEARS,'2 Years'),
    )
    order_id = models.CharField(max_length=100,unique=True)
    # amount = models.IntegerField(default=0)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='subscriptions')
    duration = models.CharField(choices=DURATION_TYPE, max_length=20)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

    def save(self, *args, **kwargs):
        ### change end_date
        if self.duration == self.SIX_MONTHS:
            self.end_date = self.start_date + datetime.timedelta(days=183)

        if self.duration == self.ONE_YEAR:
            self.end_date = self.start_date + datetime.timedelta(days=365)

        if self.duration == self.TWO_YEARS:
            self.end_date = self.start_date + datetime.timedelta(days=730)

        super().save(*args, **kwargs)


class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='payments')
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    transaction = models.CharField( max_length=50)
    success = models.BooleanField(default=False)