from django.contrib import admin
from django.conf import settings 
from django.core.validators import MinValueValidator
from django.db import models
from uuid import uuid4
from store.validators import validate_file_size
from cloudinary.models import CloudinaryField

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,  
        related_name='featured_in_collections' 
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

class Product(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators= [MinValueValidator(1)]
        )
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank=True)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']

def get_image_field():
    """Returns the appropriate image field based on the environment."""
    if settings.USE_CLOUDINARY:
        return CloudinaryField('image')
    return models.ImageField(upload_to='store/images')

class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='images'
    )
    image = get_image_field()  #  Dynamically use Cloudinary or local storage
    
class Customer(models.Model):
    phone = models.CharField(max_length=255) 
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'  
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'  
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F' 
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'), 
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ] 
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT) 
    quantity = models.PositiveSmallIntegerField()  
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
    
class address(models.Model):
    street = models.CharField(max_length=255) 
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20, default="Unknown")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # Many to one relationship so customer can have multiple delivery addresses  
   
class Cart(models.Model):
    id = models.UUIDField (primary_key = True, default=uuid4) #provides unnique 32 character identifier 
    created_at = models.DateTimeField(auto_now_add=True) 
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    
    class Meta: 
         constraints = [
            models.UniqueConstraint(fields=['cart', 'product'], name='unique_cart_product')
        ] #this replaces the deprecated unique_together constraint, preventing the same product being added to cart more than once. Multiple products should increase quantity 

class Review(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now=True)
         