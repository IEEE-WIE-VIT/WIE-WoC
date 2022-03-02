from django.shortcuts import render, redirect
from .models import BlogPost, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

def home(request):
    blogs_search = []
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        blogs_search_part1 = list(BlogPost.objects.filter(blog_title__icontains = search_keyword))
        user = User.objects.filter(username = search_keyword)[:1]
        blogs_search_part2 = list(BlogPost.objects.filter(author = user))
        blogs_search_part3 = list(BlogPost.objects.filter(blog_content__icontains = search_keyword).exclude(blog_title__icontains = search_keyword))
        blogs_search = blogs_search_part1 + blogs_search_part2 + blogs_search_part3
        if blogs_search == []:
            messages.info(request, 'No Results Found')
    blogs = list(BlogPost.objects.all())
    blogs_main = random.sample(blogs, len(blogs))
    blogs_latest = BlogPost.objects.all().order_by('-publish_date')[:4]
    blogs_popular = (sorted(blogs, key = lambda x: x.total_likes())[::-1])[:4]
    blogs_editor = random.sample(blogs_main, len(blogs_main))[:4]
    if blogs_search != []:
        blogs_main = blogs_search
    context = {
        "blogs": blogs_main,
        "tags": {
        'Finance': 'Finance',
        'Fashion': 'Fashion',
        'Politics' : 'Politics',
        'Sports' : 'Sports',
        'Travel' : 'Travel',
        'Lifestyle' : 'Lifestyle',
        'Science' : 'Science',
        'Environment' : 'Environment',
        'Technology' : 'Technology',
        },
        "blogs_popular": blogs_popular,
        "blogs_latest": blogs_latest,
        "blogs_editor": blogs_editor,
    }
    return render(request, "blogs/home.html", context)

@login_required(login_url='login')
def blog_upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            author = User.objects.get(username = request.user.username)
            blog_title = request.POST['blog_title']
            blog_content = request.POST['blog_content']
            blog_image = request.FILES.get('blog_image')
            category = Category.objects.get(category = request.POST['category'])
            blog = BlogPost.objects.create(author=author, blog_title=blog_title, blog_content=blog_content, blog_image=blog_image, category=category)
            blog.save()
            messages.info(request, 'Blog Uploaded Successfully')
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'blogs/blog_upload.html')

def blog_details(request, the_slug):
    blog_single = BlogPost.objects.get(slug=the_slug)
    total_likes = blog_single.total_likes()
    liked = False
    if blog_single.likes.filter(id = request.user.id):
        liked = True
    blogs = list(BlogPost.objects.all())
    author_blogs = list(BlogPost.objects.filter(author = blog_single.author).exclude(slug=the_slug))[:4]
    blogs_latest = BlogPost.objects.all().order_by('-publish_date')[:4]
    blogs_popular = (sorted(blogs, key = lambda x: x.total_likes())[::-1])[:4]
    context = {
        "blog_single": blog_single,
        "blog_likes": total_likes,
        "blog_liked": liked,
        "author_blogs": author_blogs,
        "blogs_popular": blogs_popular,
        "blogs_latest": blogs_latest,
    }
    return render(request, 'blogs/blog_details.html', context)

@login_required(login_url='login')
def blog_delete(request, the_slug):
    BlogPost.objects.filter(slug=the_slug).delete()
    messages.info(request, 'Blog Deleted Successfully')
    return redirect('home')

@login_required(login_url='login')
def blog_like(request, the_slug):
    blogtitle = request.POST.get('blog_title')
    blog = BlogPost.objects.get(blog_title=blogtitle)
    liked = False
    if blog.likes.filter(id = request.user.id).exists():
        blog.likes.remove(request.user)
        liked = False
    else:
        blog.likes.add(request.user) 
        liked = True
    return HttpResponseRedirect(reverse('blog_details', args=[the_slug]))