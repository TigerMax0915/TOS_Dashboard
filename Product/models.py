from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField  # RichTextField를 사용하기 위해 필요

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    representative = models.CharField(max_length=255)
    business_registration = models.FileField(upload_to='suppliers/')
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)  # Rich text 필드로 설명을 추가
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)
    shopify_id = models.CharField(max_length=255, blank=True, null=True)
    coupang_id = models.CharField(max_length=255, blank=True, null=True)
    # 추가될 수 있는 다른 플랫폼 ID 필드들...

    def __str__(self):
        return self.name

    def get_active_promotion(self):
        # 현재 활성화된 프로모션을 반환합니다.
        return self.promotions.filter(
            start_date__lte=timezone.now(), 
            end_date__gte=timezone.now(), 
            active=True
        ).first()

    def get_final_price(self):
        # 활성화된 프로모션이 있다면 할인된 가격을 계산합니다.
        promotion = self.get_active_promotion()
        if promotion:
            return promotion.apply_discount(self.selling_price)
        return self.selling_price
