from django.shortcuts import render

from . import models, utilites


def home(req):

    transmitted_data = {}
    transmitted_data.update(utilites.get_subheader_dict())
    transmitted_data.update(utilites.get_chapter_dict())

    return render(req, 'app/app.html', transmitted_data)
    

def sass (req):
        return render(req, 'app/sass.html',)