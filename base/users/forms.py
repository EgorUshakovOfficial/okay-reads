from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Login form
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

# Registration form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

