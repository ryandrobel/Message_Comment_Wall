from django.db import models
from login.models import User

# Create your models here.
class PostManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['message']) < 1 or len(post_data['message']) > 1000:
            errors['message'] = 'Post should be 1 to 1000 characters long'
        
        return errors

class Post(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class CommentManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['comment']) < 1 or len(post_data['comment']) > 1000:
            errors['comment'] = 'Comment should be 1 to 1000 characters long'
        
        return errors

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()