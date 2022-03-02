from django.urls import path
from . import views

urlpatterns = [
    path('register_customer', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<slug:profile_slug>', views.profile, name='profile'),
    path('our_team', views.our_team, name='our_team'),
    path('contact', views.contact, name='contact'),
]