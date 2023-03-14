import uuid
from django.db import models
from .Book import Book
from django.core.validators import MinValueValidator, MaxValueValidator

# Review
class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    author = models.TextField(default="Anoymous")
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return self.title