from django.contrib import admin
from . import models
from .models import Collection
from django.contrib import admin
from .models import Collection, Product, Promotion


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_product')
    fields = ('title', 'featured_product')  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'collection')
    list_editable = ['unit_price']
    fields = ('slug', 'title', 'description', 'unit_price', 'inventory', 'collection', 'promotions')
    filter_horizontal = ('promotions',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('description', 'discount')


