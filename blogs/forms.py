from django.forms import ModelForm
from blogs.models import Post, Comment

# Create the form class.
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
