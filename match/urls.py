"""LostAndFound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('lost_item',views.lost_item,name='lost_item'),
    path('lost_person',views.lost_person,name='lost_person'),
    path('found_item',views.found_item,name='found_item'),
    path('found_person',views.found_person,name='found_person'),
    path('message',views.message,name='message'),

    
]
