from django.urls import path

from accounts_users import views

urlpatterns = (
    path('register/', views.RegisterUser.as_view(), name='register-user'),
    path('login/', views.LoginUser.as_view(), name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('edit/<int:pk>', views.EditUser.as_view(), name='edit-user')
)