from django.urls import path 
from . import views

urlpatterns = [
    path('', views.product_list),
    path('<int:id>/', views.product_detail),
    path('collections/<int:id>/', views.collection_detail, name='collection-detail')

    
]