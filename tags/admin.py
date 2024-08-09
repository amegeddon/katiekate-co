from django.contrib import admin
from .models import Tag

# Define the admin class for the Tag model
class TagAdmin(admin.ModelAdmin):
    pass

# Register the model with the admin class
admin.site.register(Tag, TagAdmin)
