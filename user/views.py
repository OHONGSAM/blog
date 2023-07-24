from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm

# from django.contrib.auth.models import User
from .models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View


class UserLogin(LoginView):
    model = User
    template_name = "user/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("main")  # 로그인 성공 시 이동할 URL

    def form_valid(self, form):
        """로그인 성공 시 처리하는 메서드"""
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())

    def form_invalid(self, form):
        """로그인 실패 시 처리하는 메서드"""
        # return render(self.request, self.template_name, {'form': form, 'error_message': 'Invalid username or password'})
        return HttpResponse("wrong id or password")


class UserLogout(LogoutView):
    model = User
    next_page = "main"


class UserRegister(CreateView):
    template_name = "user/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("main")


class UserProfile(LoginRequiredMixin, UpdateView):
    model = User  # 업데이트할 모델 지정 (여기서는 User 모델 사용)
    form_class = UserProfileForm
    template_name = "user/profile.html"  # 사용할 템플릿 지정
    success_url = reverse_lazy("main")  # 업데이트 후 리다이렉트할 URL 지정

    def get_object(self, queryset=None):
        return self.request.user


class UserPWChange(LoginRequiredMixin, PasswordChangeView):
    model = User
    template_name = "user/password.html"  # 사용할 템플릿 지정
    success_url = reverse_lazy("main")  # 비밀번호 변경 후 리다이렉트할 URL 지정
