from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_gallery, name='hello_gallery'),
]
