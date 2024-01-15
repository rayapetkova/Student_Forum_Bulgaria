from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts_users.forms import RegisterUserForm, LoginUserForm


class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    form_class = LoginUserForm


class RegisterUser(CreateView):
    template_name = 'accounts/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main-page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


# class LogOutUser(auth_views.LogoutView):
#     template_name = 'accounts/logout_page.html'


def logout_user(request):
    logout(request)
    return redirect('login-user')


def main_view(request):
    return render(request, 'main_pages/after_login_main_page.html')
