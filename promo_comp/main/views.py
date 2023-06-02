from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

def index(response):
	dates = hello
	return render(response, 'index.html', dates)