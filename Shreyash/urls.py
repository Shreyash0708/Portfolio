from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("contact/", views.contact_view, name="contact"),
    path('projects/', views.Project_list, name='projects'),
    path('skillset/', views.skillset, name='skillset'),
    

] 