from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import logging
import requests

# Create your views here.
# request handlers


def hello_gallery(request):
    return render(request, 'gallery.html')

logger = logging.getLogger(__name__) 

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Ames'})
