from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import Account


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "phone_number")

        def clean_password2(self):
            pass1 = self.cleaned_data["password1"]
            pass2 = self.cleaned_data["password2"]
            if pass1 and pass2 and pass1 != pass2:
                raise forms.ValidationError('password didn"t match')
            return pass2
