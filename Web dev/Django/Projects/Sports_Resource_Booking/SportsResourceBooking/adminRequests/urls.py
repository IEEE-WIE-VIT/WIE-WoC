from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('requests/',views.requests,name='requests'),
    path('reject/<value>',views.reject,name='reject'),
     path('accept/<value>',views.accept,name='accept')
]