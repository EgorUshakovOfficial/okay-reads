from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']