from django.contrib import admin
from .models import *


admin.site.register(Manufacturer)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(WheelSize)
admin.site.register(SuspensionTravel)
admin.site.register(Material)
admin.site.register(Weight)
admin.site.register(CharacteristicTitle)
admin.site.register(CharacteristicDescription)


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


class HamletGaleryAdmin(admin.StackedInline):
    model = HamletGalery
@admin.register(Hamlet)
class HamletAdmin(admin.ModelAdmin):
    inlines = [HamletGaleryAdmin]
    class Meta:
       model = Hamlet
@admin.register(HamletGalery)
class HamletGaleryAdmin(admin.ModelAdmin):
    pass