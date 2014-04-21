from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.Form):
    animal_name = forms.CharField(max_length=256)


class UserForm(UserCreationForm):
    email = forms.EmailField()

    def save(self, commit=True):
        profile = super(UserForm, self).save(commit=False)
        profile.email = self.cleaned_data['email']
        if commit:
            profile.save()
        return profile