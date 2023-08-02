from django.contrib.auth.forms import AuthenticationForm
from django import forms

from posts.models import Post


# ----------------------------------------------------------------
class UserLoginForm(AuthenticationForm):
    """
    Login form

    Attrs:
        - username: username of user
        - password: password of user
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# ----------------------------------------------------------------
class PostForm(forms.ModelForm):
    """Form for new post"""
    class Meta:
        model = Post
        fields = ('title', 'body')
