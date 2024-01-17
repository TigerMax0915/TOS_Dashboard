from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .supplier_serializer import SupplierSerializer

# Create your views here.
class SupplierViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SupplierSerializer