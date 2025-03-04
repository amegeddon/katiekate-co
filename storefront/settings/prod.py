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


# **Cloudinary Storage Configuration**
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("dbzincfkg"),
    "API_KEY": os.environ.get("275537512889256"),
    "API_SECRET": os.environ.get("CL_UpTSW70cmcFL9O_eiDtQeU9xrs"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"