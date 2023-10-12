from django.contrib import admin
from .models import *


admin.site.register(Manufacturer)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(WheelSize)
admin.site.register(SuspensionTravel)
admin.site.register(Material)
admin.site.register(Weight)
admin.site.register(Characteristic)
admin.site.register(CharacteristicValue)


class BicycleGaleryAdmin(admin.StackedInline):
    model = BicycleGalery
@admin.register(Bicycle)
class BycicleAdmin(admin.ModelAdmin):
    inlines = [BicycleGaleryAdmin]
    class Meta:
       model = Bicycle
@admin.register(BicycleGalery)
class BycicleGaleryAdmin(admin.ModelAdmin):
    pass


class AccessorieGaleryAdmin(admin.StackedInline):
    model = AccessorieGalery
@admin.register(Accessorie)
class AccessorieAdmin(admin.ModelAdmin):
    inlines = [AccessorieGaleryAdmin]
    class Meta:
       model = Accessorie
@admin.register(AccessorieGalery)
class AccessorieGaleryAdmin(admin.ModelAdmin):
    pass