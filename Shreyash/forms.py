from django import forms
from .models import project, skill

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = project
#         fields = ['title', 'description', 'tech_stack', 'video_path', 'github_link']

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = skill
#         fields = ['name', 'icon_path']