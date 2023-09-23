from django.shortcuts import render
from .models import Chapter


def home(req):
    chapters = Chapter.objects.all()


    return render(req, 'app/app.html', {
        'chapters': chapters
    })
    

def sass (req):
        return render(req, 'app/sass.html',)