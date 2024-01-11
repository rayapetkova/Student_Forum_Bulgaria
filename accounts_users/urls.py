from django.urls import path

from accounts_users import views

urlpatterns = (
    path('register/', views.RegisterUser.as_view(), name='register-user'),
    path('login/', views.LoginUser.as_view(), name='login-user'),
    path('main_page/', views.main_view, name='main-page')
)