from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter sign'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter text'
            }),
        }