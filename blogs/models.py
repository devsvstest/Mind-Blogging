from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    likes = models.IntegerField(null = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(is_approved = True)

    def get_absolute_url(self):
        return reverse('blogs:post_detail', kwargs = {'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blogs.Post', related_name = 'comments', on_delete=models.CASCADE, null = True)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    is_approved = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse('blogs:post_list')

    def approve(self):
        self.is_approved = True
        self.save()

    def __str__(self):
        return self.text
