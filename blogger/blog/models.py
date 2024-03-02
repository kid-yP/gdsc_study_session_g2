from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.slugField(max_length=255)
    body = models.Textfield()
    def __str__(self):
        return self.title
