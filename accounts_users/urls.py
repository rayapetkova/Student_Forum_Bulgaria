from django.urls import path

from accounts_users import views

urlpatterns = (
    path('register/', views.register_user, name='register-user'),
    path('login/', views.login_user, name='login-user')
)