from rest_framework import serializers

class ProductSerializers (serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    price = serializers.DecimalField(source='unit_price', max_digits=10, decimal_places=2)