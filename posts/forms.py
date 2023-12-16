from django import forms
from .models  import Post




class CreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "group")
        labels = {'text': ('Текст поста'),
                  'group': ('Группа')}
        help_texts = {
            "text": ("Попробуйте удивить мир своими необычными идеями"),
            "group": ("Укажите группу, чтобы Ваш пост было проще найти Вашим поклонникам"),
        }
    def clean_text(self):
        text = self.cleaned_data['text']
        return text


