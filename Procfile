release: python manage.py migrate
web: waitress-serve --listen=0.0.0.0:$PORT storefront.wsgi:application
worker: python manage.py process_tasks