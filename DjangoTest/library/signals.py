from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core import cache
from .models import Book
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Book)
def log_book_creation(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Book created: {instance.title} by {instance.author.name}")

@receiver(post_delete, sender=Book)
def log_book_deletion(sender, instance, **kwargs):
    logger.info(f"Book deleted: {instance.title} by {instance.author.name}")

@receiver(post_save, sender=Book)
@receiver(post_delete, sender=Book)
def clear_books_cache(sender, instance, **kwargs):
    cache.delete('book_list_cache')