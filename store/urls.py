from django.urls import path 
from . import views

urlpatterns = [
    path('', views.product_list),
    path('<int:id>/', views.product_detail, name='product-detail'),
    path('collections/<int:pk>/', views.collection_detail, name = 'collection-detail')

    
]