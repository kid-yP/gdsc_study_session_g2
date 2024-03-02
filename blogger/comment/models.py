from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
