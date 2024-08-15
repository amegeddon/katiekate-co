from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin  import ProductAdmin
from tags.models import TaggedItem
from store.models import Product, CartItem
# Register your models here.

class TagInline(GenericTabularInline):
     autocomplete_fields = ['tag']
     model = TaggedItem   
     
class  CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]     
        
admin.site.unregister(Product)        
admin.site.register(Product, CustomProductAdmin)

#This CartItemAdmin class must be deleted before deployment, created solely to add items to cart in order to test api's working as expected 
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

admin.site.register(CartItem, CartItemAdmin)