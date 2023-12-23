# order_deliver/models.py

from django.db import models
from product.models import Product
from .constants import PLATFORM_CHOICES, DELIVERY_METHOD_CHOICES, COURIER_CHOICES
from django.utils import timezone

class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)  # 주문 번호, 고유해야 합니다.
    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)  # 주문이 이루어진 플랫폼
    order_date = models.DateTimeField(default=timezone.now)  # 주문 날짜와 시간, 기본값은 현재 시간
    customer_name = models.CharField(max_length=255)  # 고객 이름
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 주문된 제품, Product 테이블 참조
    quantity = models.PositiveIntegerField()  # 주문 수량, 양수만 가능
    platform_product_id = models.CharField(max_length=255, blank=True, null=True)  # 플랫폼별 제품 식별 번호
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # 총 주문 금액
    event_applied = models.CharField(max_length=255, blank=True, null=True)  # 적용된 이벤트 유형
    event_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 이벤트가 적용된 가격
    address = models.CharField(max_length=500)  # 배송 주소
    postal_code = models.CharField(max_length=12)  # 우편번호
    status = models.CharField(max_length=100, default='pending')  # 주문 상태, 기본값은 'pending'
    delivery_method = models.CharField(max_length=100, choices=DELIVERY_METHOD_CHOICES, default='face_to_face')  # 배송 방법
    courier = models.CharField(max_length=100, choices=COURIER_CHOICES, default='tw_post')  # 택배사
    tracking_number = models.CharField(max_length=255, blank=True, null=True)  # 송장 번호
    dispatched_date = models.DateTimeField(null=True, blank=True)  # 발송 날짜
    estimated_delivery_date = models.DateTimeField(null=True, blank=True)  # 예상 배송 도착 날짜
    delivery_date = models.DateTimeField(null=True, blank=True)  # 실제 배송 도착 날짜

    def __str__(self):
        return f"Order {self.order_number} - {self.platform} - {self.customer_name}"
    
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')  # 주문과 1:1 관계
    tracking_number = models.CharField(max_length=255, blank=True, null=True)  # 송장 번호
    dispatched_date = models.DateTimeField(null=True, blank=True)  # 배송 시작 날짜
    estimated_delivery_date = models.DateTimeField(null=True, blank=True)  # 예상 배송 도착 날짜
    delivery_date = models.DateTimeField(null=True, blank=True)  # 실제 배송 도착 날짜

    def __str__(self):
        return f"Delivery {self.tracking_number} - {self.order.order_number}"  # 객체를 문자열로 표현할 때 사용하는 메서드