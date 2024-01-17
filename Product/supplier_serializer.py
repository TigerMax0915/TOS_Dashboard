# 파일명 supplier_serializer.py

from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'representative', 'business_registration', 'email', 'phone_number', 'notes']