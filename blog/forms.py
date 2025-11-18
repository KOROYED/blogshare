from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Comment, Post

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': 'Comment'}


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','body']
        labels = {'title': 'Title',
                  'category': 'Category',
                  'body': 'Contents'}
        widgets = {
            'body': forms.Textarea(attrs={"class": "create-post"}),
        }