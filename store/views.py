from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Product
from .serialisers import ProductSerializers

# Create your views here.
@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializers(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
        product = get_object_or_404(Product, pk=id) 
        serializer = ProductSerializers(product)  
        return Response(serializer.data)  
 
    
    
    