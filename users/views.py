from typing import Any
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from carts.models import Cart
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/users.html'
    form_class = UserLoginForm
    title = 'Login'

    def get_success_url(self) -> str:
        return reverse_lazy('index')


class UserRegistrationView(TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/users.html'
    success_url = reverse_lazy('login')
    title = 'Registration'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/users.html'
    title = 'Profile'

    def get_success_url(self) -> str:
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['buskets'] = Cart.objects.filter(user=self.object)
        return context


@login_required
def logout(req):
    auth.logout(req)

    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
