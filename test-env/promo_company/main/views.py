from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def title (response):
	data = {'data': [1,2,3], 'title1' : 'title'}
	return render (response, "main/title.html",data)
def user (response):
	#return HttpResponse ("<h1> Hello world ! </h1>")
	return render (response, "main/user.html")
data1 = {'theme': 'Python','name': 'Project 1', 'descr' : 'all about python'}
def project (response):
	#return HttpResponse ("<h1> Hello world ! </h1>")
	return render (response, "main/project.html",data1)