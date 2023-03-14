from django.forms import ModelForm
from ..models import Book

# Book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover_image', 'author', 'description', 'genre', 'publication_date']