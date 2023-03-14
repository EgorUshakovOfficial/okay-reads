from django.shortcuts import redirect,render
from django.contrib import messages

# Book form
from ..forms import BookForm

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