# BlogApp/models.py
from django.db import models


class Tag(models.Model):
    name = models.charField(max_length=20)
    def __str__(self):
        return self.name


class Post(models.Model):  # Fix the typo here from models.model to models.Model
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
