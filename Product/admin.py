from django.contrib import admin
from .models import Supplier
 
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'representative', 'business_registration', 'email', 'phone_number', 'notes' ]
