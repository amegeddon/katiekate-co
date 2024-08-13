from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),

    
]