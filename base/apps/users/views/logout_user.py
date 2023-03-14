from django.shortcuts import redirect
from django.contrib.auth import logout

# Logout view
def logout_user(request):
    # Logout user
    logout(request)

    # Redirect the user back to the login page
    return redirect('login')