from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import CustomUser
from users.forms import UserLoginForm, UserRegistrationForm
from app.utilites import get_chapter_dict, get_subheader_dict


def login(req):
    if req.method == 'POST':
        form = UserLoginForm(data=req.POST)
        if form.is_valid():
            username = req.POST['username']
            password = req.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(req, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    
    context = {'form': form, 'reauest': login}
    context.update(get_chapter_dict())
    context.update(get_subheader_dict())

    return render(req, 'users/login.html', context)


def registration(req):
    if req.method == 'POST':
        form = UserRegistrationForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    context.update(get_chapter_dict())
    context.update(get_subheader_dict())

    return render(req, 'users/registration.html', context)