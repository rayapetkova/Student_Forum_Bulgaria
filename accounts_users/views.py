from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts_users.forms import RegisterUserForm, LoginUserForm

UserModel = get_user_model()


class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    form_class = LoginUserForm


class RegisterUser(CreateView):
    template_name = 'accounts/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('subjects-list')

    def form_valid(self, form):
        result = super().form_valid(form)

        permission = Permission.objects.get(codename='add_topic')
        user = UserModel.objects.get(email=form.cleaned_data['email'])

        # print("EI TUKA BE")
        # print(user)
        # print(permission)
        # print(form.cleaned_data)

        current_user_role = form.cleaned_data['role']

        if current_user_role in ('Student', 'Teacher'):
            user.user_permissions.add(permission)

        login(self.request, self.object)
        return result


# class LogOutUser(auth_views.LogoutView):
#     template_name = 'accounts/logout_page.html'


def logout_user(request):
    logout(request)
    return redirect('login-user')
