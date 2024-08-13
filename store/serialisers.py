from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Collection
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(source='unit_price', max_digits=10, decimal_places=2)
    # collection = serializers.StringRelatedField() # using just this to return collection title rather than the below for now
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection-detail'
    )
    # )   Currently this breaks the store/ pathway - cant figure out why 

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'collection']


