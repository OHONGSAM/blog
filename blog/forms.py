# blog/forms.py
from django import forms
from django_tuieditor.fields import MarkdownFormField
from django_tuieditor.widgets import MarkdownEditorWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "thumbnail", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "thumbnail": forms.ClearableFileInput(
                attrs={
                    "rows": "3",
                    "cols": "35",
                    "class": "form-control",
                    "id": "formFile",
                }
            ),
            "category": forms.Select(
                attrs={"rows": "3", "cols": "35", "class": "custom-select"}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": "3",
                    "cols": "35",
                    "class": "form-control",
                    "placeholder": "아름다운 댓글을 달아주세요",
                }
            )
        }


# <textarea class = "form-control" rows = "3"
#  placeholder = "Join the discussion and leave a comment!" > </textarea >
