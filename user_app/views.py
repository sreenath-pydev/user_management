from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# sing in
def signin(request):
    error_message=None
    
    if request.POST:
        User = request.POST['username']
        Pass = request.POST['password']
        user=authenticate(username=User,password=Pass)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message='wrong username or password'
    return render(request,'signin.html',{'error_message':error_message})

# home page
@login_required(login_url='signin/')
def home(request):
    return render(request,'home.html')

# sign out
def signup(request):
    user=None
    error_message =None
    success_message=None
    if request.POST:
        UserN = request.POST['username']
        PassW = request.POST['password']
        Email = request.POST['email']
        Re_pw = request.POST['repeat_password']
        if PassW != Re_pw:
            error_message = 'Passwords do not match'
        elif User.objects.filter(email=Email).exists():
            email_error_message = 'Email address is already registered.'
        else:
            try:
                user = User.objects.create_user(username=UserN,password=PassW,email=Email)
                success_message='User created successfully!'
        
            
            except :
                error_message= 'username alredy existing'
    return render(request,'signup.html',{'user':user,'error_message':error_message ,'success_message': success_message,'email_error_message':email_error_message})


# sign out
def signout(request):
    logout(request)
    return redirect('signin')