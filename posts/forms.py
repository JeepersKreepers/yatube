from django import forms
from .models  import Post




class CreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("group", "text", "author")


