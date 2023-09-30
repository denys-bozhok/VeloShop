from django.contrib import admin
from .models import *

 
 

admin.site.register(Color)
admin.site.register(FrameSize)
admin.site.register(WheelSize)
admin.site.register(Characteristic)
admin.site.register(Manufacturer)


class BycicleGaleryAdmin(admin.StackedInline):
    model = BicycleGalery
 
@admin.register(Bicycle)
class BicycleAdmin(admin.ModelAdmin):
    inlines = [BycicleGaleryAdmin]
 
    class Meta:
       model = Bicycle
 
@admin.register(BicycleGalery)
class BycicleGaleryAdmin(admin.ModelAdmin):
    pass



