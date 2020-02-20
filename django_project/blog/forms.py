from django import forms
from .models import Comment,Post

class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please input a title'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs = {
            "class":"form-control",
            "placeholder":"Please enter the content of your post"
        }
    ))
    # categories = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please input a category'}))
    class Meta:
        model = Post
        fields = ['title','content']

class CommentForm(forms.ModelForm):
    # author = 
    content = forms.CharField(widget=forms.Textarea(
        attrs = {
            "class":"form-control",
            "placeholder":"Please enter your comment"
        }
    ))

    class Meta:
        model = Comment
        fields = ['content']