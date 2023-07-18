from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse


class UserLogin(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')  # 로그인 성공 시 이동할 URL

    def form_valid(self, form):
        """로그인 성공 시 처리하는 메서드"""
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())

    def form_invalid(self, form):
        """로그인 실패 시 처리하는 메서드"""
        # return render(self.request, self.template_name, {'form': form, 'error_message': 'Invalid username or password'})
        return HttpResponse('wrong id or password')


class UserLogout(LogoutView):
    next_page = 'main'


class UserRegister(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
