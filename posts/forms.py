from django.contrib.auth.forms import forms


class CreatePost(forms.ModelForm):


class PostForm(forms. Form):
    group = forms.Charfield(requiredsFalse)
    text = forms.Charfield(widgetsforms.Textarea, required=True)