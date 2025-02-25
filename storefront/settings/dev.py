from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-qns=j&-y9_el+=+ofo=s+6h-1hztq8cxae28z7^5w&(1d618$9'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}