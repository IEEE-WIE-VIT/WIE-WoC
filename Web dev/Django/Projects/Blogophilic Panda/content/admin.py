from django.contrib import admin
from .models import BlogPost, Category

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Category)
