from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.urls import reverse
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from . import models
from .models import Collection
from django.contrib import admin
from .models import Collection, Product, Promotion, Customer, Order 

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_product', 'products_count')
    fields = ('title', 'featured_product')

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id) 
            })
        )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')  
        )
        
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'inventory_status', 'collection_title')
    list_editable = ['unit_price']
    list_filter= ['collection']
    list_per_page = 15
    list_select_related = ['collection']
    fields = ('slug', 'title', 'description', 'unit_price', 'inventory', 'collection', 'promotions')
    filter_horizontal = ('promotions',)
    
    def collection_title(self,product):
        return product.collection.title
        
    
    @admin.display(ordering = 'inventory')
    def inventory_status (self, product): 
        if product.inventory < 2:
            return 'Low'
        return 'OK'
    

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('description', 'discount')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_per_page = 15
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    
    @admin.register(Order)
    class OrderAdmin(admin.ModelAdmin):
        list_display = ('id', 'placed_at', 'customer')
    

