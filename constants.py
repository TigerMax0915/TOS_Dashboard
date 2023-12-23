# constants.py

# 주문이 이루어진 온라인 플랫폼 선택지
PLATFORM_CHOICES = (
    ('platform_1', '플랫폼 1'),
    ('platform_2', '플랫폼 2'),
    # 여기에 추가적인 플랫폼을 계속 추가할 수 있습니다.
)

# 배송 방법 선택지
DELIVERY_METHOD_CHOICES = (
    ('face_to_face', '대면 전달'),
    ('standard_shipping', '표준 배송'),
    # 필요한 경우 추가 배송 방법을 여기에 추가할 수 있습니다.
)

# 택배사 선택지
COURIER_CHOICES = (
    ('tw_post', 'TW우체국'),
    ('fedex', '페덱스'),
    ('ups', 'UPS'),
    # 추가적인 택배사를 여기에 등록할 수 있습니다.
)
