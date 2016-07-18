from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse

#To pass: page_title, page_author,  

def index(request):
	return render(request, 'poll/index.html', {'year':timezone.now().year, 'page_title':"Poll Engine - Create free, advanced and interactive polls",})

def login_view(request):
	username=request.POST['username']
	password=request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			#return render(request, 'poll/index.html', {'year':timezone.now().year, 'page_title':"Poll Engine - Create free, advanced and interactive polls",})
			return redirect('index')
		else:
			#A disabled account
			return HttpResponse("Your account have been disabled")
	else:
		return HttpResponse("Wrong Credentials")

@login_required
def logout_view(request):
	logout(request)
	return HttpResponse("logout successful")