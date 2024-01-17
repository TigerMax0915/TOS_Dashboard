from django.db import models
from Product.models import Product
from datetime import date

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_rate = models.FloatField()
    description = models.TextField()
    # 기타 필요한 필드들...

# PromotionProduct 모델로 어떤 product가 관련 promotion에 해당하는지 확인
class PromotionProduct(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)  # 주요 제품 여부
    # 기타 필요한 필드

# PromotionProduct 모델로 어떤 product가 관련 promotion에 해당하는지 확인
class PromotionCondition(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    required_product = models.ForeignKey(Product, related_name='required_product', on_delete=models.CASCADE)
    required_quantity = models.IntegerField(default=1)
    discount_product = models.ForeignKey(Product, related_name='discount_product', on_delete=models.CASCADE)
    discount_rate = models.FloatField()  # 할인율
    # 기타 필요한 필드

class DiscountVoucher(models.Model):
    code = models.CharField(max_length=100)
    discount_rate = models.FloatField()
    valid_from = models.DateField()
    valid_until = models.DateField()
    is_used = models.BooleanField(default=False)

    def apply_discount(self, order_total):
        if self.is_valid() and not self.is_used:
            return order_total * (1 - self.discount_rate)
        return order_total

    def is_valid(self):
        today = date.today()
        return today >= self.valid_from and today <= self.valid_until


