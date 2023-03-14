import uuid
from django.db import models

# Book
class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(default="")
    author = models.TextField(default="")
    description = models.TextField(default="")
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    cover_image = models.FileField(upload_to='media/', null=True)

    # Genre choices
    class Genre(models.TextChoices):
        ART = "art", "Art"
        CHILDREN = "childrens", 'Children\'s'
        CLASSIC = "classic", 'Classic'
        SCIENCE_FICTION = "science-fiction", 'Science Fiction'
        THRILLER  = "thriller", 'Thriller'
        BIOGRAPHY = "biography", 'Biography'
        CHRISTIAN = "christian", 'Christian'
        SCIENCE = "science", 'Science'
        SELF_HELP = "self-help", 'Self Help'

    genre = models.CharField(max_length=40, choices=Genre.choices, default=Genre.ART[0])

    def get_genres(self):
        return self.Genre.choices

    def __str__(self):
        return self.title