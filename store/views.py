from django.db.models.aggregates import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Collection, OrderItem
from .serialisers import ProductSerializer, CollectionSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class =  ProductSerializer  
 
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response ({'error': 'This item cannot be deleted currently as it is associated with an order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
         return super().destroy(request, *args, **kwargs)
     
class CollectionViewSet(ModelViewSet) :
    queryset =  queryset =  Collection.objects.annotate(
            products_count=Count('products')).all()
    serializer_class = CollectionSerializer  
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']):
            return Response({'error': 'Collection cannot be deleted at this time because it is associated with one or more products'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)
    
  


   
