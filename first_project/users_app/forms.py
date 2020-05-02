from django import forms
from django.core import validators

def check_for_name_validation_custom(name):
    if "0" <= name[0] <= "9":
        raise forms.ValidationError("Name cannot start with a digit")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_name_validation_custom])
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # password = forms.PasswordInput
    # the 3rd parameter is for adding builtin validatoe that ensures the hidden input has at most length 0

    # user defined basic validator for hidden input botcatcher
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher

    # a clean for the whole form
    def clean(self):
        all_clean_data = super().clean()# donno why, but super().clean() returns only CharField not email
        self.email
        print("The dictionary is " + str(len(all_clean_data)))
        for key in all_clean_data.keys():
            print(str(key) + " ")
        # mail = all_clean_data['email']
        # vemail = all_clean_data['verifyEmail']
        #
        # if mail != vemail:
        #     raise form.ValidationError("Make sure emails match!")
