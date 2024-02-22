from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView

from typing import Any

from app import utilites
from common.views import TitleMixin
from carts.models import Cart
from users.models import User, EmailVerification
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


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Email verification done'
    template_name = 'users/includes/_email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(
            user=user, code=code)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verifited_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
