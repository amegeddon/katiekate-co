from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:id>/', views.ProductDetail.as_view()),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.collection_detail, name = 'collection-detail')

    
]