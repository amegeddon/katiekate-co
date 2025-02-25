from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-qns=j&-y9_el+=+ofo=s+6h-1hztq8cxae28z7^5w&(1d618$9'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_EMAIL_FROM = 'katiekate2021@outlook.com'