from django.shortcuts import render


def home(req):
    return render(req, 'app/app.html')