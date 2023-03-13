from django.forms import ModelForm
from .models import Review, Book

# Review form
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'comment', 'rating']

# Book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover_image', 'author', 'description', 'genre', 'publication_date']