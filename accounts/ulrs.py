from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # 이 줄이 accounts 앱의 urls.py를 포함하는 부분입니다.
    # 여기에 다른 앱의 URL conf를 추가할 수 있습니다.
]