from rest_framework.serializers import ModelSerializer,Serializer
from payments.models import Subscription
from payments.models import Package, PackageFeature
from rest_framework import serializers



class SelectPakageSerializer(Serializer):
    package  = serializers.ChoiceField(choices=[p.id for p in Package.objects.all()])
    duration = serializers.ChoiceField(choices=Subscription.DURATION_TYPE)


class PackageFeatureSerializer(ModelSerializer):
    class Meta:
        model = PackageFeature
        fields = ['id','title']

class PackageSerializer(ModelSerializer):

    features = PackageFeatureSerializer(many=True, read_only=True)
    class Meta:
        model = Package
        fields = [
            'id','title',
            'package_type',
            'currency',
            'six_months_price',
            'one_year_price',
            'two_years_price',
            'description',
            'features']

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id' ,
            'user' ,
            'amount',
            'package',
            'start_date',
            'end_date']
