from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, unique=True)
    last_modified = models.DateTimeField(auto_now= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_posts')
    content = models.TextField()

    class Meta:
        ordering = ['-last_modified']


class PostImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='files/')
    description = models.TextField(null=True, blank=True)

