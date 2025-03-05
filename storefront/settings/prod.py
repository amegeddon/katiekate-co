import os
from .common import *
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api


DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost']

CSRF_TRUSTED_ORIGINS = [
    "https://katiekate-prod-6e661edd389c.herokuapp.com",
]


SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config()
}

EMAIL_HOST = os.environ['TRISTI_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['TRISTI_SMTP_USER'] 
EMAIL_HOST_PASSWORD = os.environ['TRISTI_SMTP_PASSWORD']  
DEFAULT_EMAIL_FROM = 'katiekate2021@outlook.com'


CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),
}


DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
MEDIA_URL = "/media/" 