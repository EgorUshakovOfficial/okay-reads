from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Models
from ..models import Book, Review

# Review form
from ..forms import ReviewForm

# Book page view
def book_page(request, book_id):
    if request.user.is_authenticated == False:
        messages.add_message(request, messages.INFO, 'You need to log in to view this route')
        return redirect('login')

    # Finds specified book in the database
    try:
        book = get_object_or_404(Book, book_id=book_id)

    # Otherwise, handles error and redirects user to the 404 page
    except:
        return redirect('not_found')

    # Post request
    if request.method == "POST":

        # Instance of the review form
        form = ReviewForm(request.POST)

        # Form is valid
        if form.is_valid():
            # Author's full name
            author_name = f'{request.user.first_name} {request.user.last_name}'

            # Create new reviews, but does not save it to the database
            new_review = form.save(commit=False)

            # Author's name
            new_review.author = author_name

            # Specified Book
            new_review.book = book

            # Save instance of the review to the database
            new_review.save()

    # Reviews of the book
    reviews = Review.objects.filter(book=book.book_id)

    # Review form
    form = ReviewForm()

    # Context
    context = {
        'reviews': reviews,
        'book': book,
        'form': form
    }

    return render(request, 'book/book-page.html', context)