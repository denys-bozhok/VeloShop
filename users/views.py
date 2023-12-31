from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from app.utilites import subheader


def login(req):
    title = 'Login'
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
    
    context = {'form': form, 'title': title}
    context.update(subheader(req))
    return render(req, 'users/users.html', context)


def registration(req):
    title = 'Registration'
    if req.method == 'POST':
        form = UserRegistrationForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form, 'title': title}
    context.update(subheader())
    return render(req, 'users/users.html', context)


@login_required
def profile(req):
    title = 'Profile'

    if req.method == 'POST':
        form = UserProfileForm(instance=req.user, data=req.POST, files=req.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        
    else:
        form = UserProfileForm(instance=req.user)

    context = {'form': form, 
               'title': title,
               }
    
    context.update(subheader(req))
    
    return render(req, 'users/users.html', context)


@login_required
def logout(req):
	auth.logout(req)

	return HttpResponseRedirect(reverse('index'))