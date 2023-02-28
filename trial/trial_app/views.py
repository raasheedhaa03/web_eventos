from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import auth
from tce_event_web import settings
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,"user/index.html")

def signup(request):
	if request.method=="POST":
		username=request.POST.get('name')
		reg_no=request.POST['regno']
		email=request.POST.get('email')
        dept=request.POST['dept']
        ph_no=request.POST['ph_no']
		password=request.POST.get('password')
		confpassword=request.POST.get('confpassword')
		if User.objects.filter(username=username):
			messages.error(request,"This username already exists")
			return redirect('signup')
		if User.objects.filter(email=email).exists():
			messages.error(request,"This email already exists")
			return redirect('signup')
		EmailValidator()(email)
		domain = email.split('@')[1]
		if domain != 'student.tce.edu':
			messages.error(request,"Enter your student mail id")
			return redirect('signup')
		if password != confpassword:
			return redirect('signup')
		user=User.objects.create_user(username,email,password)
		user.first_name=first_name
		user.save()
		return redirect('login')
	return render(request,'user/signup.html')


def login(request):
    if request.method=='GET':
        return render(request,'user/login.html')
    else:
        user = auth.authenticate(username=request.POST.get('name'),password = request.POST.get('password'))

        if user is not None:
            auth.login(request,user)
            return render(request,'user/success.html')
        else:
            return render (request,'user/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'user/login.html')
