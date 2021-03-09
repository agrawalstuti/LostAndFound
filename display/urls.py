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
    
    path('lost_item_case',views.lost_item_case,name='lost_item_case'),
    path('lost_person_case',views.lost_person_case,name='lost_person_case'),
    path('found_item_case',views.found_item_case,name='found_item_case'),
    path('found_person_case',views.found_person_case,name='found_person_case'),
    path('detail_lost_item/<id>',views.detail_lost_item,name='detail_item'),
    path('detail_lost_person/<id>',views.detail_lost_person,name='detail_person'),
    path('detail_found_item/<id>',views.detail_found_item,name='detail_item'),
    path('detail_found_person/<id>',views.detail_found_person,name='detail_person'),
    path('lost_item_case/<cname>',views.lost_item_category,name='lost_item_case'),
    path('lost_person_case/<cname>',views.lost_person_category,name='lost_person_case'),
    path('found_item_case/<cname>',views.found_item_category,name='found_item_case'),
    path('found_person_case/<cname>',views.found_person_category,name='found_person_case'),
]
