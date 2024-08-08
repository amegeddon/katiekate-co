from django.contrib import admin
from . import models
from .models import Collection


# Register your models here.
admin.site.register(models.Collection)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_product')
    fields = ('title', 'featured_product')  
