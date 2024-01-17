from django.contrib import admin
from .models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'discount_rate', 'description')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')


