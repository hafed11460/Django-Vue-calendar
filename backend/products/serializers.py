from rest_framework.serializers import ModelSerializer
from products.models import Package,PackageFeature

class PackageFeatureSerializer(ModelSerializer):
    class Meta:
        model = PackageFeature
        fields = ['id','title']
class PackageSerializer(ModelSerializer):
    features = PackageFeatureSerializer(many=True, read_only=True)
    class Meta:
        model = Package
        fields = ['id','name','monthly_price','annual_price','features']
        # fields = '__all__'