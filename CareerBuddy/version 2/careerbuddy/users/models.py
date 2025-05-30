from django.db import models

class Profile(models.Model):
    user = models.CharField(max_length=100)
    bio = models.TextField()
