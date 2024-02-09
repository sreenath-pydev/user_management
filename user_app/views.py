from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    user=None
    error_massage =None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,password=password)
        except :
            error_massage= 'username alredy existing'
    return render(request,'signup.html',{'user':user,'error_massage':error_massage})