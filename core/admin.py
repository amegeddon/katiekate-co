from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin  import ProductAdmin
from tags.models import TaggedItem
from store.models import Product, CartItem
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )

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
    
    
# #this too to be deleted as just created to allow for orders to be created and test api 
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'unit_price', 'order_id', 'product')

admin.site.register(CartItem, CartItemAdmin)