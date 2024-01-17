from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include, path


router = DefaultRouter()
router.register('supplier', views.SupplierViewset)

urlpatterns = [
    path('', include(router.urls)),
]