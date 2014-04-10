from django import forms


class PostForm(forms.Form):
    animal_name = forms.CharField(max_length=256)