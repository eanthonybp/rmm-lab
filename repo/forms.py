from django import forms
from django.forms import ModelForm
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','snippet','category']
