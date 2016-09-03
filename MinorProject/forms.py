from django import forms

from .models import Users


class UserForms(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            "email_id",
            "password",
        ]
        widgets = {'email_id': forms.TextInput(attrs={'placeholder': 'Email ID'}),
                   'password': forms.TextInput(attrs={'type': "password", 'placeholder': 'Password'})}


class Contact(forms.Form):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    message = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'message', 'placeholder': 'Message'}))
