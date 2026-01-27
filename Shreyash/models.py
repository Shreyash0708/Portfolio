from django.db import models
from django.contrib.auth.models import User

class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
# Create your models here.
class skill(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name