from django import forms
from django.core import validators
from signup_app.models import new_user

class NewUserForm(forms.ModelForm):
    class Meta():
        model = new_user
        fields = '__all__'
