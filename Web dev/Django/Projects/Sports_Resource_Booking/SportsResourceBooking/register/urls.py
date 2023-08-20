from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('login_action',views.login_action,name='login_action'),
    path("logout",views.logout,name="logout"),
]