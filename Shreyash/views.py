from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
# from .models import project
# from .forms import ProjectForm, SkillForm
from django.shortcuts import redirect, get_object_or_404


# def Project_list(request):
#     projects = projects.objects.all().order_by('title')
#     return render(request, 'projects.html', {'projects': projects})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Message from {name}"
        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,   # from
            [settings.EMAIL_HOST_USER], # to (your email)
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def skillset(request):
    return render(request, 'skillset.html')
def projects(request):
    return render(request, 'projects.html')