from django.contrib import admin
from . import models
from .models import Collection
from django.contrib import admin
from .models import Collection, Product, Promotion, Customer


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_product')
    fields = ('title', 'featured_product')  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'collection', 'inventory_status')
    list_editable = ['unit_price']
    list_per_page = 15
    fields = ('slug', 'title', 'description', 'unit_price', 'inventory', 'collection', 'promotions')
    filter_horizontal = ('promotions',)
    
    
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

