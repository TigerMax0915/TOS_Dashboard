from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active', 'is_superuser']
    # 필요한 경우 list_filter, search_fields 등을 설정할 수 있습니다.