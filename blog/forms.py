# blog/forms.py
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "category": forms.TextInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            )
        }
