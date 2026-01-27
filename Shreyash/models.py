from django.db import models
from django.contrib.auth.models import User
from django.db import models

class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)

    # CHANGED: Use CharField to store the path (e.g., 'videos/demo.mp4')
    video_path = models.CharField(max_length=200, blank=True, null=True, help_text="Path relative to static folder (e.g. 'videos/demo.mp4')")
    
    # CHANGED: Same for images
    # image_path = models.CharField(max_length=200, blank=True, null=True, help_text="Path relative to static folder (e.g. 'images/project1.png')")
    
    github_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class skill(models.Model):
    name = models.CharField(max_length=100)
    # CHANGED: Store path to icon/logo
    icon_path = models.CharField(max_length=200, blank=True, null=True, help_text="Path relative to static folder (e.g. 'skills/python.png')")

    def __str__(self):
        return self.name