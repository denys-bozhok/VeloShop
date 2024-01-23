from django.db import models
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    image = models.FileField(upload_to='images/users', blank=True, null=True)
    is_verifited_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'{EmailVerification} for {self.user.email}'

    def send_verification_email(self):
        link = reverse('verify', kwargs={
                       'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Confirm email for {self.user.username}'
        massage = f'For confirm email {
            self.user.email} click on the link {verification_link}'

        send_mail(subject, massage, 'from@example.com',
                  recipient_list=[self.user.email], fail_silently=False,)

    def is_expired(self):
        return True if now() >= self.expiration else False
