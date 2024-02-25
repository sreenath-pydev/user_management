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
    if request.POST:
        UserN = request.POST['username']
        PassW = request.POST['password']
        try:
            user = User.objects.create_user(username=UserN,password=PassW)
            
        except :
            error_message= 'username alredy existing'
    return render(request,'signup.html',{'user':user,'error_message':error_message})


# sign out
def signout(request):
    logout(request)
    return redirect('signin')