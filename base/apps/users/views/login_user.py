from django.shortcuts import render, redirect
from ..forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Login view
def login_user(request):
    # Post method
    if request.method == "POST":
        # Retrieve username and password values
        username = request.POST.get('username')
        password = request.POST.get('password1')

        # Attempt to sign in user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Login user
            login(request, user)

            # Redirect the user to the home page
            return redirect('index')

        # Display error message to the user
        messages.add_message(request, messages.ERROR, 'Username or password is incorrect')


    # Instantiate empty sign-in form
    form = LoginForm()

    context = {'form': form}

    return render(request, 'users/signin.html', context)