from django.urls import path

from accounts_users import views

urlpatterns = (
    path('register/', views.RegisterUser.as_view(), name='register-user'),
    path('login/', views.LoginUser.as_view(), name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('edit/', views.EditUser.as_view(), name='edit-user'),
    path('details/', views.ProfileDetails.as_view(), name='details-user'),
    path('delete/', views.DeleteProfile.as_view(), name='delete-user')
)