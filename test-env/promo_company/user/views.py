from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest
from usermanag.forms import CustomUserCreationForm, LoginForm, ChangeUser
from django.contrib.auth import get_user_model

user = get_user_model()

def yep(request):
    return render(request, "yep.html")

def reg(request):

    if request.method == "GET":
        return render(
            request, "reg.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "yep.html")
        else:
            data = form.errors
            print(data)
            return render(request, "no.html", {'data' : data})

def no(request):
    return render(request, "no.html")


def user_page(request):

    if request.method == "POST":
        form = ChangeUser(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
    form = ChangeUser()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['phone_number'].initial = request.user.phone_number
    form.fields['email'].initial = request.user.email
    data = {'form':form}
    return render(request, "user_page.html", data)