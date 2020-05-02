from django import forms
from django.contrib.auth.models import User
from userAuth_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    # password = forms.PasswordInput()
    password = forms.CharField(widget=forms.PasswordInput())
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

        class Meta():
            model = UserProfileInfo
            fields = ('portfolio_site','profile_pic')
