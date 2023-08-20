from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('addInfo/',views.addInfo,name='addInfo'),
    
]