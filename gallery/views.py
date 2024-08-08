from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handlers


def hello_gallery(request):
    return HttpResponse("Hello - your gallery will appear here")

