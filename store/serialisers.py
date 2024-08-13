from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(source='unit_price', max_digits=10, decimal_places=2)
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )
