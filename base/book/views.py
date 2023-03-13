from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Models
from .models import Book, Review

# Review form
from .forms import ReviewForm, BookForm

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


# Creates new book
def add_book(request):
    # Protects add book form route
    if request.user.is_authenticated == False:
        messages.add_message(request, messages.INFO, 'You need to log in to view this route')
        return redirect('login')

    # Post request
    if request.method == "POST":
        # Instance of the book form
        form = BookForm(request.POST, request.FILES)

        # Form is valid
        if form.is_valid():
            # Save instance of the new book in the database
            form.save()

            # Redirect to the home route
            return redirect('index')

    # Instance of the book form
    form = BookForm()

    context = {'form': form}

    return render(request, 'book/add-book.html', context)

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