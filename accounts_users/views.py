from django.contrib.auth import views as auth_views
from django.shortcuts import render


class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login_page.html'


def register_user(request):
    return render(request, 'accounts/register_page.html')


def login_user(request):
    return render(request, 'accounts/login_page.html')


def main_view(request):
    return render(request, 'main_pages/after_login_main_page.html')
