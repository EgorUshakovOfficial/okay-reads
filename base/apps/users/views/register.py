from django.shortcuts import render, redirect
from ..forms import RegistrationForm
from django.contrib import messages

# Registration view
def register(request):
    # POST request
    if request.method == "POST":
        # Instance of the registration form
        form = RegistrationForm(request.POST)

        # Form is valid
        if form.is_valid():
            # Save new user in the database
            form.save()

            # Add success message and redirect user to the login page
            messages.add_message(request, messages.SUCCESS, "New user is successfully registered and may now log in.")

            # Redirect user to the login page
            return redirect('login')

        # Add error message and refresh the page
        messages.add_message(request, messages.ERROR, "Registration failed. Please try again")


    form = RegistrationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)
