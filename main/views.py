from django.shortcuts import render,redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


def homepage(request):
	return render(request=request,
					template_name='main/home.html',
					context={'tutorials':Tutorial.objects.all})


def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()#registering
			username=form.cleaned_data.get('username')
			messages.info(request,"New Account Created: %s" %username)
			login(request,user)
			return redirect('/')
		else:
			for msg in form.error_messages:
				messages.error(request," %s"%form.error_messages[msg])



			return render(request,
							'main/register.html',
							{'form':form})


	form=UserCreationForm
	return render(request,
					'main/register.html',
					{'form':form})


def logout_request(request):
	logout(request)
	messages.warning(request,"logged out successfully!")
	return redirect('/')

def login_request(request):
	if request.method=='POST':
		form=AuthenticationForm(request,request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username,password)
			if user is not None:
				login(request,user)
				messages.info(request,'You are logged in as %s'%username)
				return redirect('/')
			else:
				messages.error(request,"invaid username or password")
		else:
			messages.error(request,"invaid username or password")

	#get request		

	form=AuthenticationForm()
	return render(request,
					'main/login.html',
					{'form':form})