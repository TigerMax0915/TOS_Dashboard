## accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # AbstractUser에서 제공하는 필드를 그대로 사용합니다.
    # 여기에 추가 필드를 정의하지 않았으므로, 기본 필드만 사용됩니다.
    
    # Django의 기본 User 모델과 충돌을 피하기 위해 related_name을 설정합니다.
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_set",
        related_query_name="user",
    )
    
    # 추가 필드 없이 기본 필드만을 사용합니다.
    pass

    def __str__(self):
        return self.username