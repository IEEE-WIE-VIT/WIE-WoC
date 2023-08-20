from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html') 

def login_action(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = auth.authenticate( username=username,password=password,email=role)

        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('/register/login')

def logout(request):
    auth.logout(request)
    return redirect('/') 

def signin(request):

    if request.method == 'POST':
        
        name = request.POST['name']        
        idno = request.POST['idno']       
            
        phno = request.POST['phno']
        role = request.POST['role']
      
        password1  = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 : 

            if User.objects.filter(username=idno).exists():
                messages.info(request, "Email already registered")
                return redirect('/register/signup')
            else:
                
                user = User.objects.create_user(first_name=name,email=role,username=idno,last_name=phno,password=password1)
                user.save()
                print("User created")   
                return redirect('/register/login') 
                     
        else:
            print("Password not matching....")
            return redirect('/register/signup')
       

