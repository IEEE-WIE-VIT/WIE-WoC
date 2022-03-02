from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from content.models import BlogPost, Category
from .models import Profile, Contact

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        image = request.FILES.get('profile_pic')
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_customer')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password = password1)
                profile = Profile.objects.create(user = user, image = image)
                user.save()
                profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request, profile_slug):
    profile = Profile.objects.get(slug = profile_slug)
    user = User.objects.get(username = profile)
    blogs = BlogPost.objects.filter(author = user)
    context = {
        "blogs": blogs,
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
        "profile_det": profile,
        "user_det": user,
    }
    return render(request, "accounts/profile.html", context)

def our_team(request):
    return render(request, "our_team.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        messages = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.save()
        messages.info(request, 'Message sent successfully. Thank you for writing to us.')
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')