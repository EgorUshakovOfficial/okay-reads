from django.shortcuts import render
from django.db.models import Q

# Models
from book.models import Book

# Helpers
from .helpers.get_ratings import get_ratings

def index(request, *args, **kwargs):
    # Search filter and genre query parameters
    query = request.GET.get('query', '')
    genre = request.GET.get('genre', '')

    # Books
    books = Book.objects.all()

    # Filter by title or description
    if query != "":
        books = books.filter(Q(title__icontains=query) | Q(description__icontains=query))

    # Filter by genre
    if genre != "":
        books = books.filter(genre=genre)

    # Ratings
    ratings = get_ratings(books)

    # Genres of books
    genres = Book.get_genres(self=Book)

    context = {
        'genres': genres,
        'books': books,
        'ratings': ratings,
        'query': query,
        'genre': genre
    }

    return render(request, 'main/index.html', context)

def page_not_found(request):
    return render(request, 'page-not-found.html', {})