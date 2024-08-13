from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Product, Collection
from .serialisers import ProductSerializer, CollectionSerializer

# Create your views here.
@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(
        queryset, many=True, context = {'request': request})
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
        product = get_object_or_404(Product, pk=id) 
        serializer = ProductSerializer(product)  
        return Response(serializer.data)  
 
@api_view()
def collection_detail(request, id):
    collection = get_object_or_404(Collection, pk=id) 
    serializer = CollectionSerializer(collection) 
    return Response(serializer.data)
    
    
    