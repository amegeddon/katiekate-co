from django.contrib import admin
from . import models
from .models import Collection
from django.contrib import admin
from .models import Collection, Product, Promotion, Customer, Order 


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_product')
    fields = ('title', 'featured_product')  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'inventory_status', 'collection_title')
    list_editable = ['unit_price']
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
    
    @admin.register(Order)
    class OrderAdmin(admin.ModelAdmin):
        list_display = ('id', 'placed_at', 'customer')
    

