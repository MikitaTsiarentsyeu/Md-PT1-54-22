from random import choices
from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False, primary_key=True)

class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('p', 'public license')]

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(choices=POST_TYPES, max_length=1)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

