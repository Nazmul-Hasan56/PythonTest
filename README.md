#start Django server
python manage.py runserver

#start celery worker
celery -A DjangoTest worker -l info

#start Celery beat for periodic tasks
celery -A DjangoTest worker -l info


install dependencies
'rest_framework',
'rest_framework.authtoken',
'django_filters',
'library'
