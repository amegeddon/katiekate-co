from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handlers


def hello_gallery(request):
    return render(request, 'gallery.html')

