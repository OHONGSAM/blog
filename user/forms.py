from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password", "profile_img"]
        widgets = {
            "username": forms.TextInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "password": forms.PasswordInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "profile_img": forms.ClearableFileInput(
                attrs={
                    "rows": "3",
                    "cols": "35",
                    "class": "form-control",
                    "id": "formFile",
                }
            ),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "profile_img"]
        widgets = {
            "username": forms.TextInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
            "profile_img": forms.ClearableFileInput(
                attrs={"rows": "3", "cols": "35", "class": "form-control"}
            ),
        }
