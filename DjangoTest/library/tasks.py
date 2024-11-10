from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from .models import Book


@shared_task
def archive_old_books():
    ten_years_ago = timezone.now.date() - timedelta(days=365 * 10)
    Book.objects.filter(published_date__lt=ten_years_ago)