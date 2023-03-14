import uuid
from django.db import models
from apps.book.models import Book

# Author
class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.CharField(max_length=50, default='')
    bio = models.TextField()
    books = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.author_name








