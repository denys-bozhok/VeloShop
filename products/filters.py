from queryset_sequence import QuerySetSequence

from .models import *


def bicycles_filter(req):
    bicycles = Bicycle.objects.all()
    wheel = req.GET.get('wheel')
    size = req.GET.get('size')

    try:
        if size:
            bicycles = bicycles.filter(frame_size=Size.objects.get(short_name=size).id)

        if wheel:
            bicycles = bicycles.filter(wheel=WheelSize.objects.get(size=float(wheel)).id)
            
    except:
        return bicycles
    
    return bicycles

    


def accessories_filter(req):
    accessories = Accessorie.objects.all()

    return accessories


def components_filter(req):
    components = Component.objects.all()

    return components


def filters(req, *model_name):
    try:
        match(model_name[0]):
            case 'Bicycles':
                return bicycles_filter(req)
            
            case 'Accessories':
                return accessories_filter(req)
            
            case 'Components':
                return components_filter(req)
            
            case 'Workshop':
                return bicycles_filter(req)
            
    except:
        return QuerySetSequence(Bicycle.objects.all(), 
                                Accessorie.objects.all(), 
                                Component.objects.all())