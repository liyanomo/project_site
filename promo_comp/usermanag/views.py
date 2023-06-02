from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from usermanag.forms import CustomUserCreationForm, LoginForm, ChangeUser
from django.contrib.auth import get_user_model

# Create your views here.

user = get_user_model()

def dashboard(request):
	return render(request, 'dashboard.html')


def register(request):
	if request.method == 'GET':
		return render(request, 'register.html', 
			{'form': CustomUserCreationForm}
			)
	elif request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return render(request, 'dashboard.html')
		else:
			data = form.errors
			print(data)
			return render(request, 'error.html', {'data': data})


def error(request):
	return render(request, 'error.html')


def profile(request):
	if request.method == 'POST':
		form = ChangeUser(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	form = ChangeUser()

	data = {'form': form}
	return render(request, 'profile.html', data)