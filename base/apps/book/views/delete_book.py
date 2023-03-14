from django.shortcuts import redirect
from django.contrib import messages
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Models
from ..models import Book

# Delete specified book
def delete_book(request, book_id):
    # Attempts to delete specified book
    try:
        # Deletes specified book from the database
        Book.objects.filter(book_id=book_id).delete()

    except:
        # Attach some kind of message here...
        print('Something went wrong. Unable to delete specified book')

    finally:
        return redirect('index')


# Signal-after specified book is deleted, specified image from S3
@receiver(post_delete, sender=Book)
def delete_cover_image(sender, instance, **kwargs):
    instance.cover_image.delete(False)
