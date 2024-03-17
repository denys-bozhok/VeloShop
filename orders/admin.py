from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'created', 
        ('owner_name', 'owner_surname'),
        ('email', 'adress', 'city'),
        'status', 'user', 'order_info',
    )
    readonly_fields = ('id', 'created')