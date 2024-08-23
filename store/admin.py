from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.urls import reverse
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from .models import Collection, Product, Promotion, Customer, OrderItem, Order, ProductImage    

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
            products_count=Count('products')  
        )
        
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['title']
    }
    inlines = [ProductImageInline]
    list_display = ('title', 'unit_price', 'inventory_status', 'collection_title')
    list_editable = ['unit_price']
    list_filter= ['collection', 'last_update']
    list_per_page = 15
    list_select_related = ['collection']
    fields = ( 'title', 'slug', 'description', 'unit_price', 'inventory', 'collection', 'promotions')
    filter_horizontal = ('promotions',)
    
    def collection_title(self,product):
        return product.collection.title
        
    
    @admin.display(ordering = 'inventory')
    def inventory_status (self, product): 
        if product.inventory < 2:
            return 'Low'
        return 'OK'
    
    class Media:
        css = {
            'all': ['store/styles.css']
        }
    

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('description', 'discount')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name')
    list_per_page = 15
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = OrderItem 
    extra = 1 
    min_num = 1
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ('id', 'payment_status', 'placed_at', 'customer')
    inlines = [OrderItemInline] 
    

