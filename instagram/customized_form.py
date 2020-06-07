from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from instagram.models import User

# Implementing registration based on User model fields. Reduced redundancy of defining fields already defined in the
# User model by using ModelForms - forms based on models
# Application: make forms based on model fields in database-driven apps
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'user_avatar', 'email']