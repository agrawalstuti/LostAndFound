
#from __future__ import unicode_literals

#from collections import OrderedDict

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = (
            'email','username','firstname','lastname',
            'adhaar_no','address','city','state','pin','phone_no','password1','password2')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password',widget=forms.PasswordInput)

    class Meta :
        model = Account
        fields = ('email','password')

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")