from django.db import models


class Notes(models.Model):
    title   = models.CharField(max_length=255)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True) 
    last_update = models.DateTimeField(auto_now=True)
