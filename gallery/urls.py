from django.urls import path
from . import views
from .views import HelloView
import requests

urlpatterns = [
    path('', views.hello_gallery, name='hello_gallery'),
    path('hello/', HelloView.as_view(), name='hello'),
]
