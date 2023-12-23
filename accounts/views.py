# accounts/views.py

from django.urls import reverse_lazy   #url 패턴이름을 기반으로 URL을 지연평가 지원
from django.views import generic
from django.contrib.auth.views import LoginView #사용자 로그인을 처리하는 뷰임
# `CustomUserCreationForm`은 `forms.py`에서 정의한 사용자 생성 폼을 가져옴
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'  # 경로 변경

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # 경로 변경
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')  # 사용자 로그인 후 이동할 페이지 URL 지정