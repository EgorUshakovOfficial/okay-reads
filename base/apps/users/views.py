# from django.shortcuts import render, redirect
# from .forms import RegistrationForm, LoginForm
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages

# Login view
# def login_user(request):
#     # Post method
#     if request.method == "POST":
#         # Retrieve username and password values
#         username = request.POST.get('username')
#         password = request.POST.get('password1')

#         # Attempt to sign in user
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             # Login user
#             login(request, user)

#             # Redirect the user to the home page
#             return redirect('index')

#         # Display error message to the user
#         messages.add_message(request, messages.ERROR, 'Username or password is incorrect')


#     # Instantiate empty sign-in form
#     form = LoginForm()

#     context = {'form': form}

#     return render(request, 'users/signin.html', context)

# # Logout view
# def logout_user(request):
#     # Logout user
#     logout(request)

#     # Redirect the user back to the login page
#     return redirect('login')

# Registration view
# def register(request):
#     # POST request
#     if request.method == "POST":
#         # Instance of the registration form
#         form = RegistrationForm(request.POST)

#         # Form is valid
#         if form.is_valid():
#             # Save new user in the database
#             form.save()

#             # Add success message and redirect user to the login page
#             messages.add_message(request, messages.SUCCESS, "New user is successfully registered and may now log in.")

#             # Redirect user to the login page
#             return redirect('login')

#         # Add error message and refresh the page
#         messages.add_message(request, messages.ERROR, "Registration failed. Please try again")


#     form = RegistrationForm()

#     context = {'form': form}

#     return render(request, 'users/register.html', context)
